from app.schemas.signUpSchema import SignUpSchema
from sqlalchemy.orm import Session

class SignUpRepository:
    def create(self, db: Session, *, data: SignUpSchema):
        print("repo",data)
        return True