from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from app.errors.models import ResponseErrorModel


class CurrencyError(HTTPException):
    def __init__(self, status_code: int = 404, detail: str = 'Currency not found'):
        super().__init__(status_code=status_code, detail=detail)


async def currency_error_handler(request, exc: CurrencyError) -> JSONResponse:
    detail = ResponseErrorModel(
        message=exc.detail,
    ).model_dump()
    return JSONResponse(
        status_code=exc.status_code,
        content={'error': detail}
    )
