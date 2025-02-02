import asyncio

import pytest_asyncio
import pytest
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.cofig import settings
from httpx import AsyncClient, ASGITransport
from app.db.database import Base
from main import app

url = 'http://127.0.0.1:8000'
data = {'username': 'test', 'password': 'test'}
new_data = {'username': 'test', 'password': 'testtest'}


@pytest_asyncio.fixture(scope="session")
async def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='function', autouse=True)
async def setup_database():
    if settings.MODE == "TEST":
        engine = create_async_engine(settings.DB_URL, echo=True)

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        yield
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)


@pytest.mark.asyncio
async def test_register():
    async with AsyncClient(transport=ASGITransport(app=app), base_url=url) as client:
        response = await client.post('/auth/reg', json=new_data)
        assert response.status_code == 201
        assert response.json().get('success')

        response = await client.post('/auth/reg', json=data)
        assert response.status_code == 422


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(transport=ASGITransport(app=app), base_url=url) as client:
        response = await client.post("/auth/log-in", json=new_data)
        assert response.status_code == 401

        response = await client.post("/auth/log-in", json=data)
        assert response.status_code == 422
