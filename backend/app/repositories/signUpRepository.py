# app/repositories/signUpRepository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.models.user import User

class SignUpRepository:
    async def create(self, db: AsyncSession, user) -> User:
        uid = user.get("uid")
        email = user.get('email')
        obj = User(id=uid, email=email)
        db.add(obj)
        try:
            await db.commit()
            await db.refresh(obj)
            return obj
        except IntegrityError:
            await db.rollback()
            raise
