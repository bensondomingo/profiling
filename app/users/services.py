from typing import Coroutine
from sqlalchemy import select, delete, desc, update
from sqlalchemy.ext.asyncio import AsyncSession
from .schema import ProfileCreateSchema, RelationType
from .models import Profile, Relation


async def list_profiles(db: AsyncSession) -> Coroutine[None, None, list[Profile]]:
    stmt = select(Profile).order_by(desc(Profile.created_at))
    res = await db.execute(statement=stmt)
    profiles = res.scalars().all()
    await db.commit()
    return profiles


async def create_profile(
    profile: ProfileCreateSchema,
    db: AsyncSession,
) -> Coroutine[None, None, Profile]:
    obj = Profile(**profile.dict())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def update_profile(
    profile_id: int, profile: ProfileCreateSchema, db: AsyncSession
) -> Coroutine[None, None, Profile]:
    stmt = select(Profile).filter_by(id=profile_id)
    res = await db.execute(statement=stmt)
    profile_obj = res.scalar_one()

    stmt = (
        update(Profile)
        .where(Profile.id == profile_id)
        .values(**profile.dict())
        .returning(Profile)
    )
    await db.execute(stmt)
    await db.commit()
    await db.refresh(profile_obj)
    return profile_obj


async def delete_profile(
    profile_id: int,
    db: AsyncSession,
) -> Coroutine[None, None, None]:
    obj = await db.get(Profile, ident=profile_id)
    await db.delete(obj)
    await db.commit()


async def add_relation(
    profile_id: int,
    relative_id: int,
    relation_type: RelationType,
    db: AsyncSession,
) -> Coroutine[None, None, Relation]:
    obj = Relation(type=relation_type, subject_id=profile_id, relative_id=relative_id)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def remove_relation(
    profile_id: int,
    relative_id: int,
    relation_type: RelationType,
    db: AsyncSession,
):
    stmt = delete(Relation).where(
        Relation.subject_id == profile_id,
        Relation.relative_id == relative_id,
        Relation.type == relation_type,
    )
    await db.execute(statement=stmt)
    await db.commit()
