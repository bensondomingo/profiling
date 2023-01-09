from datetime import date
from typing import Optional

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.models import Base, CommonFieldsMixin


class Profile(CommonFieldsMixin, Base):
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[Optional[str]] = mapped_column(
        String(50),
        default=None,
        unique=True,
    )
    contact_number: Mapped[Optional[str]] = mapped_column(
        String(11),
        default=None,
        unique=True,
    )
    address: Mapped[Optional[str]] = mapped_column(JSONB, default=dict)
    birth_date: Mapped[Optional[date]] = mapped_column(default=None)

    marital_status: Mapped[Optional[str]] = mapped_column(default=None)
    gender: Mapped[Optional[str]] = mapped_column(default=None)

    relations: Mapped[list['Relation']] = relationship(
        back_populates='subject',
        primaryjoin='Profile.id==Relation.subject_id',
    )
    relatives: Mapped[list['Relation']] = relationship(
        back_populates='relative',
        primaryjoin='Profile.id==Relation.relative_id',
    )


class Relation(CommonFieldsMixin, Base):
    type: Mapped[str] = mapped_column(String(10))

    subject_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    subject: Mapped[Profile] = relationship(
        back_populates='relations',
        primaryjoin='Relation.subject_id==Profile.id',
    )

    relative_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    relative: Mapped[Profile] = relationship(
        back_populates='relatives',
        primaryjoin='Relation.relative_id==Profile.id',
    )

    __table_args__ = (UniqueConstraint('type', 'subject_id', 'relative_id'),)
