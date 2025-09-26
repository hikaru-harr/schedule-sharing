import json
import os
import firebase_admin
from firebase_admin import credentials, auth
from app.core.config import settings

_initialized = False

def init_firebase() -> None:
    print("init_firebase")
    """環境変数から認証情報を読み、Admin SDK を一度だけ初期化。"""
    cred = credentials.Certificate("/Users/hikaru.sugita/myapp/schedule-sharing/backend/schedule-sharing-20479-firebase-adminsdk-fbsvc-2d71cb9acc.json")
    firebase_admin.initialize_app(cred)

def verify_id_token(id_token: str):
    """
    FirebaseのIDトークンを検証してclaims(dict)を返す。
    署名/iss/aud/exp 等の検証を Admin SDK が行う。
    """
    init_firebase()
    return auth.verify_id_token(id_token)

def verify_id_token_strict(id_token: str):
    """
    失効・無効化（revoked/disabled）もチェックしたい場合はこちら。
    その分オンライン照会が入る可能性あり。
    """
    init_firebase()
    return auth.verify_id_token(id_token, check_revoked=True)
