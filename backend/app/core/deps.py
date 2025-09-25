# app/core/deps.py
from typing import Generator
from sqlalchemy.orm import Session
from app.core.db import SessionLocal
def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
