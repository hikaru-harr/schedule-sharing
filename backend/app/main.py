from fastapi import FastAPI
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI + uv")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
def health():
    return {"status": "ok"}