from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_session
from app.services.signUpService import SignUpService
from app.schemas.signUpSchema import SignUpSchema
from app.repositories.signUpRepository import SignUpRepository
from typing import Annotated

router = APIRouter(prefix="/signup", tags=["signup"])

def get_signUp_service():
    return SignUpService(repo=SignUpRepository())

DB = Annotated[Session, Depends(get_session)]
SVC = Annotated[SignUpService, Depends(get_signUp_service)]

@router.post("", status_code=201)
def signup(payload: SignUpSchema, db: DB, svc: SVC):
    print("router", payload)
    result = svc.create(db, data=payload)
    print("router return", result)
    return {"ok": True}