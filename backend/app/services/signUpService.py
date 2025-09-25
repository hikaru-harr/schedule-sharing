from app.repositories.signUpRepository import SignUpRepository
from sqlalchemy.orm import Session

class SignUpService:
    def __init__(self, repo: SignUpRepository):
        self.repo = repo
    
    def create(self, db: Session, *, data):
        print('service')
        repo = self.repo.create(db, data=data)
        print('service return', repo)
        return True