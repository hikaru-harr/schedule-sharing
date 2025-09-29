# app/services/signUpService.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.signUpRepository import SignUpRepository
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

class SignUpService:
    def __init__(self, repo: SignUpRepository):
        self.repo = repo

    async def create(self, db: AsyncSession, user):
        try:
            return await self.repo.create(db, user=user)
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
