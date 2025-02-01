from pydantic import BaseModel, constr, ConfigDict


class User(BaseModel):
    model_config = (ConfigDict(from_attributes=True))
    username: constr(min_length=3)
    password: constr(min_length=8)


class ReToken(BaseModel):
    refresh_token: str


class JWTToken(BaseModel):
    access_token: str


class TOKENS(ReToken, JWTToken):
    pass


class Currencies(BaseModel):
    currencies: dict[str, float]


class ListOfCurrencies(BaseModel):
    currencies: dict[str, str]
