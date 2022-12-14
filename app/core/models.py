from typing_extensions import Annotated
from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import text
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
)

int_pk = Annotated[int, mapped_column(primary_key=True, nullable=False)]
uuid_pk = Annotated[
    UUID,
    mapped_column(
        primary_key=True,
        default=uuid4,
        server_default=text('gen_random_uuid()'),
        nullable=False,
    ),
]
created_ts = Annotated[
    datetime,
    mapped_column(
        default=datetime.utcnow,
        nullable=False,
        server_default=text('current_timestamp'),
    ),
]
updated_ts = Annotated[
    datetime,
    mapped_column(
        default=datetime.utcnow,
        server_default=text('current_timestamp'),
        onupdate=text("current_timestamp"),
        nullable=False,
    ),
]


class Base(DeclarativeBase):
    """
    sqlalchemy base model
    """


class CommonFieldsMixin:

    id: Mapped[int_pk]
    created_at: Mapped[created_ts]
    updated_at: Mapped[updated_ts]

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
