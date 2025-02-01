from app.utils.unitofwork import IUnitOfWork
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.api.schemes.schemes import User
from app.core.security import hash_password, verify_password


class CRUDService:

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add(self, data: User):
        data.password = hash_password(data.password)
        try:
            async with self.uow:
                await self.uow.crud.add(data.model_dump())
                await self.uow.commit()
        except IntegrityError:
            raise HTTPException(400, 'User already exists')

    async def get(self, data: User):
        async with self.uow:
            result = await self.uow.crud.get(data.username)
            if not result or not verify_password(data.password, result.password):
                raise HTTPException(404, 'User not found')
        return result
