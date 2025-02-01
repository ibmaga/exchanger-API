from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemes.schemes import User
from app.db.models import UserInDB


class BaseCRUD(ABC):
    @abstractmethod
    async def add(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get(self, username: str):
        raise NotImplementedError

    @abstractmethod
    async def update(self, username: str, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, data: dict):
        raise NotImplementedError


class CRUD(BaseCRUD):
    model: UserInDB = UserInDB

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, data: dict):
        self.session.add(self.model(**data))

    async def get(self, username: str):
        return await self.session.get(self.model, username)

    async def update(self, username: str, data: User):
        result = await self.session.get(self.model, username)
        if result:
            result.username = data.username
            result.password = data.password
            return result

    async def delete(self, data: dict):
        result = await self.session.get(self.model, data)
        if result:
            await self.session.delete(result)
