from uuid import UUID

from fastapi import APIRouter, Depends
from app.models.user import User
from app.db.database import AsyncSession, get_session
from datetime import datetime, UTC
import uuid

from sqlalchemy import select 


router = APIRouter(prefix="/accounts", tags=["accounts"])

@router.get("/user/{user_id}")
async def get_user(user_id : uuid.UUID, session : AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).where(User.user_id == user_id))
    return result.scalar_one_or_none()


@router.post("/user")
async def create_user(session : AsyncSession = Depends(get_session)):
    user = User()
    user.email = "harshal@example.com"
    user.username = "harshal"
    user.password_hash = "hashed_password_here"
    user.is_active = True
    user.created_at = datetime.now(UTC)
    user.updated_at = None
    user.last_login_at = None
    user.is_verified = False
    user.verified_at = None

    session.add(user)
    await session.commit()