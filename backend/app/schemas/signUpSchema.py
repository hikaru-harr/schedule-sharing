from pydantic import BaseModel, Field, EmailStr

class SignUpSchema(BaseModel):
    email: EmailStr = Field(..., description="ログイン用メールアドレス")
    password: str = Field(min_length=8, max_length=128)

    model_config = {
        "extra": "forbid"
    }