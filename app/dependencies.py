from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import Session, sessionmaker

from .core.db import async_engine, sync_engine


async def get_db_session():
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


def get_session():
    with AsyncSession(async_engine) as session:
        yield session


def get_sync_session():
    with Session(sync_engine) as session:
        yield session
