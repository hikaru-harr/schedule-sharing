# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field, field_validator
from typing import Any

class Settings(BaseSettings):
    # --- App / CORS ---
    ENV: str = "dev"
    API_PREFIX: str = "/api"
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    # --- DB ---
    PG_HOST: str = "localhost"  # ← アプリはホスト実行なので localhost
    PG_PORT: int = 5432
    PG_USER: str = "postgres"
    PG_PASSWORD: str = "postgres"
    PG_DB: str = "appdb"
    SQL_ECHO: bool = False

    # Pydantic v2 の設定（.env を読む）
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # .env から "http://a,http://b" のようなカンマ区切りでも受け取れるようにする（任意）
    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def _split_cors(cls, v: Any) -> Any:
        if isinstance(v, str):
            # JSON文字列ならそのままPydanticが解釈するので、カンマ区切りっぽい時だけ処理
            if "," in v and not v.strip().startswith("["):
                return [s.strip() for s in v.split(",") if s.strip()]
        return v

    @computed_field  # type: ignore[misc]
    @property
    def DATABASE_URL(self) -> str:
        # asyncpg ドライバ
        return (
            f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASSWORD}"
            f"@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB}"
        )

settings = Settings()
