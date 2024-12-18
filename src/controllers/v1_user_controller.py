import http
from datetime import datetime, timedelta

from fastapi import APIRouter

from models.exceptions import UnauthorizedException
from requests.user_requests import LoginRequest
from responses.responses import GenericResponse
from responses.user_responses import LoginResponse, Login
from services.auth_service import AuthService

router = APIRouter(prefix="/v1/user", tags=["v1/user"])

@router.get("/ping", status_code=http.HTTPStatus.OK, response_model=GenericResponse)
async def ping():
    return GenericResponse(
        status_code=http.HTTPStatus.OK,
        error=None,
        message="Pong!",
        data=None
    )

"""Example of request, response, and exception classes"""
@router.post("/login", status_code=http.HTTPStatus.OK, response_model=LoginResponse)
async def login(req: LoginRequest):
    if AuthService.is_user_authorized(req.user, req.password):
        return LoginResponse(
            status_code=http.HTTPStatus.OK,
            error=None,
            message="Login successful!",
            data=Login(token="TOKEN_STRING", expire_at=datetime.now() + timedelta(1))
        )

    raise UnauthorizedException("Action Unauthorized!")
