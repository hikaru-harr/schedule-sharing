# app/middleware/firebase_auth.py
import json
from typing import Iterable, Optional, Sequence
from starlette.types import ASGIApp, Receive, Scope, Send
from firebase_admin import auth
from app.core.firebase import init_firebase, verify_id_token

class FirebaseAuthMiddleware:
    def __init__(
        self,
        app: ASGIApp,
        public_paths: Optional[Sequence[str]] = None,
        require_auth_by_default: bool = True,
        check_revoked: bool = False,     # 必要に応じて True（性能コストあり）
        tenant_id: Optional[str] = None, # マルチテナントなら指定
    ):
        self.app = app
        self.public_paths = tuple(public_paths or ())
        self.require_auth_by_default = require_auth_by_default
        self.check_revoked = check_revoked
        self.tenant_id = tenant_id

    def _is_public(self, path: str, method: str) -> bool:
        # CORS プリフライトは常に通す
        if method == "OPTIONS":
            return True
        return any(path.startswith(p) for p in self.public_paths)

    async def __call__(self, scope, receive, send):
            if scope["type"] != "http":
                return await self.app(scope, receive, send)

            path = scope.get("path", "")
            method = scope.get("method", "GET")
            headers = scope.get("headers", [])

            # ★ state.user を必ず初期化
            state = scope.setdefault("state", {})
            state.setdefault("user", None)

            # 認証が必要か？
            needs_auth = self.require_auth_by_default and not self._is_public(path, method)

            # Authorization 取り出し（頑健版）
            auth_header = None
            for k, v in headers:
                if k.decode().lower() == "authorization":
                    auth_header = v.decode().strip()
                    break

            token = None
            if auth_header:
                parts = auth_header.split()
                if len(parts) >= 2 and parts[0].lower() == "bearer":
                    token = parts[1]

            if not token and needs_auth:
                return await self._reject(send, 401, "Missing bearer token")

            if token:
                try:
                    decoded = auth.verify_id_token(token, check_revoked=self.check_revoked)
                    state["user"] = {
                        "uid": decoded.get("uid") or decoded.get("sub"),
                        "email": decoded.get("email"),
                        "email_verified": decoded.get("email_verified"),
                        "claims": decoded,
                    }
                except Exception as e:
                    if needs_auth:
                        return await self._reject(send, 401, f"Invalid token: {e}")
                    # 公開パスなら user=None のまま続行

            return await self.app(scope, receive, send)
    async def _reject(self, send: Send, status: int, msg: str):
        payload = {"error": {"message": msg}}
        await send({
            "type": "http.response.start",
            "status": status,
            "headers": [(b"content-type", b"application/json; charset=utf-8")],
        })
        await send({
            "type": "http.response.body",
            "body": json.dumps(payload, ensure_ascii=False).encode(),
        })
