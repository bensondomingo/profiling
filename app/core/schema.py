from typing import Any
from pydantic import BaseModel


class FieldError(BaseModel):
    field: str
    value: Any
    error: str
