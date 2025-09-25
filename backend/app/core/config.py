from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ENV: str = "dev"
    API_PREFIX: str = "/api"
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173","http://127.0.0.1:5173"]
    # DATABASE_URL: str = "sqlite:///./dev.db"  # 後でMySQLに差し替え可
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()