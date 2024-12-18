from typing import Any

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.responses import JSONResponse
from typing_extensions import Optional


class GenericResponse(BaseModel):
    status_code: int
    error: Optional[str]
    message: Optional[str]
    data: Any

    def to_json(self):
        json = jsonable_encoder(self)
        return JSONResponse(content=json, status_code=self.status_code)