import enum
from datetime import date
from typing import Optional
from uuid import UUID

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.models import Base, CommonFieldsMixin

prefix = 'user'


class MaritalStatus(enum.Enum):
    SINGLE = 'single'
    MARRIED = 'married'
    SEPARATED = 'separated'
    WIDOWED = 'widowed'


class Gender(enum.Enum):
    MALE = 'male'
    FEMALE = 'female'


class RelationType(enum.Enum):
    MOTHER = 'mother'
    FATHER = 'father'
    SPOUSE = 'spouse'
    SIBLING = 'sibling'


class Profile(CommonFieldsMixin, Base):
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[Optional[str]] = mapped_column(String(50), default=None)
    contact_number: Mapped[Optional[str]] = mapped_column(
        String(11),
        default=None,
    )
    address: Mapped[Optional[str]] = mapped_column(default=None)
    contact_number: Mapped[Optional[str]] = mapped_column(default=None)
    birth_date: Mapped[Optional[date]] = mapped_column(default=None)

    marital_status: Mapped[Optional[MaritalStatus]] = mapped_column(
        Enum(MaritalStatus),
        default=None,
    )
    gender: Mapped[Optional[Gender]] = mapped_column(
        Enum(Gender),
        default=None,
    )
    relations: Mapped[list['Relation']] = relationship(
        back_populates='subject',
        primaryjoin='Profile.id==Relation.subject_id',
    )
    relatives: Mapped[list['Relation']] = relationship(
        back_populates='relative',
        primaryjoin='Profile.id==Relation.relative_id',
    )


class Relation(CommonFieldsMixin, Base):
    type: Mapped[RelationType] = mapped_column(Enum(RelationType))

    subject_id: Mapped[UUID] = mapped_column(ForeignKey('profile.id'))
    subject: Mapped[Profile] = relationship(
        back_populates='relations',
        primaryjoin='Relation.subject_id==Profile.id',
    )

    relative_id: Mapped[UUID] = mapped_column(ForeignKey('profile.id'))
    relative: Mapped[Profile] = relationship(
        back_populates='relatives',
        primaryjoin='Relation.relative_id==Profile.id',
    )

    # relative_id: UUID = Field(foreign_key=f'{prefix}_profiles.id')
    # relative: Profile = Relationship(
    #     back_populates='relatives',
    #     sa_relationship_kwargs={
    #         'primaryjoin': 'Relation.relative_id==Profile.id',
    #         'lazy': 'joined',
    #     },
    # )
