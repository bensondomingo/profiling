from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

from app.config import settings

DB_URI_SYNC = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
    settings.DB_USER,
    settings.DB_PASSWORD,
    settings.DB_HOST,
    settings.DB_NAME,
)

DB_URI_ASYNC = 'postgresql+asyncpg://{}:{}@{}/{}'.format(
    settings.DB_USER,
    settings.DB_PASSWORD,
    settings.DB_HOST,
    settings.DB_NAME,
)

sync_engine = create_engine(DB_URI_SYNC, echo=True, future=True)
async_engine = create_async_engine(DB_URI_ASYNC, echo=True, future=True)
