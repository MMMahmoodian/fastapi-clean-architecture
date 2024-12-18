import http

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from controllers import v1_user_controller, v2_user_controller
from models.exceptions import UnauthorizedException
from responses.responses import GenericResponse

app = FastAPI()

# Importing controller
app.include_router(v1_user_controller.router)
app.include_router(v2_user_controller.router)

# Exception handling
@app.exception_handler(RequestValidationError)
async def pydantic_validation_exception_handler(request, exc):
    return GenericResponse(
        status_code=http.HTTPStatus.UNPROCESSABLE_ENTITY,
        error=exc.errors()[0]["msg"],
        message=None,
        data=None
    ).to_json()

@app.exception_handler(UnauthorizedException)
async def pydantic_validation_exception_handler(request, exc):
    return GenericResponse(
        status_code=http.HTTPStatus.UNAUTHORIZED,
        error=str(exc),
        message=None,
        data=None
    ).to_json()