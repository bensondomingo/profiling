from datetime import date
import enum
from typing import Optional

# from sqlmodel import Field, Enum

from ..core.models import Model

prefix = 'user'


class MaritalStatus(enum.Enum):
    SINGLE = 'single'
    MARRIED = 'married'
    SEPARATED = 'separated'
    WIDOWED = 'widowed'


class Gender(enum.Enum):
    MALE = 'male'
    FEMALE = 'female'


class Profile(Model, table=True):
    __tablename__ = f'{prefix}_profiles'

    first_name: str
    last_name: str
    email: Optional[str] = None
    contact_number: Optional[str] = None
    birth_date: Optional[date] = None
    address: Optional[str] = None

    marital_status: MaritalStatus
    gender: Gender
