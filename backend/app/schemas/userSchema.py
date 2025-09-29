from pydantic import BaseModel, Field, EmailStr

class FirebaseDecodedSchema(BaseModel):
    uid: str = Field(..., description="firebaseのユニークID")
    email: EmailStr = Field(..., description="email")


    model_config = {
        "extra": "forbid"
    }