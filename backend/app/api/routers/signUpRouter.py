from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.services.signUpService import SignUpService
from app.schemas.signUpSchema import SignUpSchema
from app.repositories.signUpRepository import SignUpRepository
from typing import Annotated
from app.core.firebase import verify_id_token



router = APIRouter(prefix="/signup", tags=["signup"])

def get_signUp_service():
    return SignUpService(repo=SignUpRepository())

DB = Annotated[Session, Depends(get_db)]
SVC = Annotated[SignUpService, Depends(get_signUp_service)]

@router.post("", status_code=201)
async def signup(request: Request, db: DB, svc: SVC):
    user = request.state.user
    try:
        result = await svc.create(db, user=user)   # ← await
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="failed to sign up")
    return {"ok": True, "id": getattr(result, "id", None)}