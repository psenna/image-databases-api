import os

import pytest_asyncio
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'True'

from typing import Generator
from fastapi.testclient import TestClient
from tests.factories.user_factory import UserFactory
from app.app import app
from app.run_migration import run_migrations_test

@pytest_asyncio.fixture(scope="function")
def client() -> Generator:
    run_migrations_test()
    with TestClient(app) as c:
        yield c

@pytest_asyncio.fixture(scope="function")
def database() -> Generator:
    run_migrations_test()
    yield None

@pytest_asyncio.fixture(scope="function")
async def super_user_token_header() -> Generator:
    yield await UserFactory.get_super_user_token_headers()

@pytest_asyncio.fixture(scope="function")
async def regular_user_token_header() -> Generator:
    yield await UserFactory.get_regular_user_token_headers()