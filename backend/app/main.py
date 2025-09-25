from fastapi import FastAPI, Request
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, EmailStr
from app.api.routers import signUpRouter

app = FastAPI(title="FastAPI + uv")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(signUpRouter.router)

@app.get("/health")
def health():
    return {"status": "ok"}