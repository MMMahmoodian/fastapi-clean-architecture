from pydantic import BaseModel


class LoginRequest(BaseModel):
    user: str
    password: str