from pydantic import BaseModel, EmailStr


class SCreateUserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: str
