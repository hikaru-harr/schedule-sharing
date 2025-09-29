from pydantic import BaseModel, Field, EmailStr

class SignUpSchema(BaseModel):
    idToken: str = Field(..., description="firebase認証用のidToken")

    model_config = {
        "extra": "forbid"
    }