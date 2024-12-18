from datetime import datetime

from pydantic import BaseModel

from responses.responses import GenericResponse

class Login(BaseModel):
    token: str
    expire_at: datetime

class LoginResponse(GenericResponse):
    data: Login

