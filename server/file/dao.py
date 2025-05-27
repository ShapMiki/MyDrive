from dao.base import BaseDAO
from database import async_session_maker
from file.models import File
from sqlalchemy import select, insert
from datetime import datetime


class FileDAO(BaseDAO):
    model = File

    #TODO: ПРимер, убрать
    @classmethod
    async def find_by_owner(cls, owner: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(owner=owner)
            result = await session.execute(query)
            return result.scalars().all()