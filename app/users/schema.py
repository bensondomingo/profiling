import enum
from datetime import date, datetime

from pydantic import BaseModel


class MaritalStatusSchema(str, enum.Enum):
    SINGLE = 'single'
    MARRIED = 'married'
    SEPARATED = 'separated'
    WIDOWED = 'widowed'


class Gender(str, enum.Enum):
    MALE = 'male'
    FEMALE = 'female'


class RelationType(enum.Enum):
    MOTHER = 'mother'
    FATHER = 'father'
    SPOUSE = 'spouse'
    SIBLING = 'sibling'


class ProfileBaseSchema(BaseModel):
    first_name: str
    last_name: str
    email: str | None = None
    contact_number: str | None = None
    address: str | None = None
    birth_date: date | None = None
    marital_status: MaritalStatusSchema | None = None
    gender: Gender | None = None


class ProfileListSchema(ProfileBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ProfileCreateSchema(ProfileBaseSchema):
    """"""


class RelationSchema(BaseModel):
    relative_id: int
    type: RelationType


class RelationListSchema(RelationSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class RelationCreateSchema(RelationSchema):
    """"""
