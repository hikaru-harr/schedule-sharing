from fastapi import FastAPI, Request
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, EmailStr
from app.api.routers import signUpRouter
from app.middleware.firebaseAuthMiddleware import FirebaseAuthMiddleware
from app.core.firebase import init_firebase

app = FastAPI(title="FastAPI + uv")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,  # 例: ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2) Firebase 認証（/health などは公開）
app.add_middleware(
    FirebaseAuthMiddleware,
    public_paths=["/health", "/docs", "/openapi.json"],
    require_auth_by_default=True,
    check_revoked=False,
)

app.include_router(signUpRouter.router)

@app.on_event("startup")
def _startup():
    init_firebase()

@app.get("/health")
def health():
    return {"status": "ok"}