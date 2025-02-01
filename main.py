from fastapi import FastAPI

from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.currency import router as currency_router
from app.errors.handlers import currency_error_handler, CurrencyError

app = FastAPI()

app.add_exception_handler(CurrencyError, currency_error_handler)
app.include_router(auth_router)
app.include_router(currency_router)
