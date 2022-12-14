import enum
from datetime import date, datetime

import arrow
from pydantic import BaseModel, validator


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


class AddressSchema(BaseModel):
    unit_number: str | None = None
    street: str | None = None
    purok: str | None = None
    brgy: str | None = None
    municipality: str | None = None
    provice: str | None = None

    class Config:
        orm_mode = True


class ProfileBaseSchema(BaseModel):
    first_name: str
    last_name: str
    email: str | None = None
    contact_number: str | None = None
    address: AddressSchema | None = None
    birth_date: date | None = None
    marital_status: MaritalStatusSchema | None = None
    gender: Gender | None = None


class ProfileListSchema(ProfileBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    @validator('address', pre=True)
    def deserialize_json_address(cls, v: str | None):
        """
        Convert json string to AddressShema type
        """
        value = AddressSchema.parse_raw(v)
        return value

    class Config:
        orm_mode = True


class ProfileCreateSchema(ProfileBaseSchema):
    """"""

    @validator('birth_date', pre=True)
    def deserialize_datetime(cls, v: str | None):
        try:
            return arrow.get(v).datetime
        except Exception:
            return v


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
