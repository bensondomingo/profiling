from app.config import settings
from sqlalchemy.ext.asyncio import create_async_engine

DB_URI_ASYNC = 'postgresql+asyncpg://{}:{}@{}/{}'.format(
    settings.DB_USER,
    settings.DB_PASSWORD,
    settings.DB_HOST,
    settings.DB_NAME,
)


async_engine = create_async_engine(DB_URI_ASYNC, echo=True, future=True)
