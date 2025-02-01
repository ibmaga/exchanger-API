from fastapi import APIRouter, Depends

from app.core.security import get_payload
from app.services.external_api import REQ
from app.errors.models import ResponseErrorModel
from app.api.schemes.schemes import Currencies, ListOfCurrencies

router = APIRouter(
    prefix='/currency',
    tags=['currency']
)

@router.get('/exchanges/', status_code=200, responses={404: {'model': ResponseErrorModel}})
async def fresh_currencies(source: str, payload: dict = Depends(get_payload)) -> Currencies:
    return REQ.get_fresh_currency(source)

@router.get('/list/', status_code=200)
async def list_of_currencies(payload: dict = Depends(get_payload)) -> ListOfCurrencies:
    return ListOfCurrencies(currencies=REQ.get_currency_list())