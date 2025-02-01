from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials

from app.api.schemes.schemes import JWTToken, User
from app.core.security import create_jwt
from app.services.crud_process import CRUDService
from app.utils.unitofwork import IUnitOfWork, UnitOfWork

router = APIRouter(
    prefix='/auth',
    tags=['auth & users']
)


async def get_crud_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> CRUDService:
    return CRUDService(uow)


@router.post('/reg', status_code=201)
async def register(user: Annotated[HTTPBasicCredentials, User], crud: CRUDService = Depends(get_crud_service)):
    await crud.add(User.model_validate(user))
    return {'success': 'True'}


@router.post('/log-in', status_code=200)
async def login(user: Annotated[HTTPBasicCredentials, User], crud: CRUDService = Depends(get_crud_service)) -> JWTToken:
    await crud.get(User.model_validate(user))
    token = await create_jwt({'sub': user.username})
    return JWTToken(access_token=token)

# @router.get('/refresh-token', status_code=200)
# async def refresh_token() -> JWTToken:
#     token = await create_jwt()
#     return JWTToken(access_token=token)
