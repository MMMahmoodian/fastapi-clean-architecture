import http

from fastapi import APIRouter

from responses.responses import GenericResponse

router = APIRouter(prefix="/v2/user", tags=["v2/user"])

"""If you have breaking changes you need to add a new version. 
Just like this example we changed the method from get to post 
and since its a breaking change we created new api in v2"""
@router.post("/ping", status_code=http.HTTPStatus.OK, response_model=GenericResponse)
async def ping():
    return GenericResponse(
        status_code=http.HTTPStatus.OK,
        error=None,
        message="Pong from v2!",
        data=None
    )


