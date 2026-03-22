from pydantic import BaseModel, EmailStr, Field


class SCreateUserRequest(BaseModel):
    username: str = Field(..., min_length=5)
    password: str = Field(..., min_length=8)
    email: EmailStr
