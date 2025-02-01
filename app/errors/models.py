from pydantic import BaseModel


class ResponseErrorModel(BaseModel):
    message: str
