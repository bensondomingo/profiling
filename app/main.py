from typing import List
from uuid import UUID
from fastapi import Depends, FastAPI
from sqlalchemy import select
from app.users.models import Gender, Profile

from pydantic import BaseModel, UUID4

from .dependencies import get_sync_session, Session


app = FastAPI()


class ProfileOutput(BaseModel):
    id: UUID4
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


@app.get('/', response_model=List[ProfileOutput])
async def read_root(db: Session = Depends(get_sync_session)):
    stmt = select(Profile)
    res = db.execute(stmt)
    profiles = res.scalars().all()
    return profiles
