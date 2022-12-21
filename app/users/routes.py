from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.utils import parse_integrity_error

from ..dependencies import get_db_session
from . import services as srv
from .models import Profile
from .schema import (
    ProfileCreateSchema,
    ProfileListSchema,
    RelationType,
    RelationListSchema,
    RelationCreateSchema,
)

router = APIRouter(prefix='/profiles', tags=['profiles'])


@router.get(path='/', response_model=list[ProfileListSchema])
async def profiles(db: AsyncSession = Depends(get_db_session)):
    stmt = select(Profile)
    res = await db.execute(statement=stmt)
    profiles = res.scalars().all()
    await db.commit()
    return profiles


@router.post(path='/', response_model=ProfileListSchema)
async def create_profile(
    profile: ProfileCreateSchema,
    db: AsyncSession = Depends(get_db_session),
):
    try:
        profile = await srv.create_profile(profile=profile, db=db)
    except IntegrityError as e:
        errors = parse_integrity_error(err_msgs=e.args)
        raise HTTPException(status_code=400, detail=[e.dict() for e in errors])
    return profile


@router.delete(path='/{profile_id}', response_model=None, status_code=204)
async def delete_profile(profile_id: int, db: AsyncSession = Depends(get_db_session)):
    await srv.delete_profile(profile_id=profile_id, db=db)


@router.post(
    path='/{profile_id}/relations',
    response_model=RelationListSchema,
    status_code=201,
)
async def add_relation(
    profile_id: int,
    relation_data: RelationCreateSchema,
    db: AsyncSession = Depends(get_db_session),
):
    try:
        obj = await srv.add_relation(
            profile_id=profile_id,
            relative_id=relation_data.relative_id,
            relation_type=relation_data.type.value,
            db=db,
        )
    except IntegrityError as e:
        errors = parse_integrity_error(err_msgs=e.args)
        raise HTTPException(status_code=400, detail=[e.dict() for e in errors])
    else:
        return obj


@router.delete(
    path='/{profile_id}/relations/{relative_id}',
    response_model=None,
    status_code=204,
)
async def remove_relation(
    profile_id: int,
    relative_id: int,
    relation_type: RelationType,
    db: AsyncSession = Depends(get_db_session),
):
    await srv.remove_relation(
        profile_id=profile_id,
        relative_id=relative_id,
        relation_type=relation_type.value,
        db=db,
    )
