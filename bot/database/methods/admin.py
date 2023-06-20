from aiogram.types import Message
from sqlalchemy import select

from bot.database.methods.base import BaseDBService
from bot.database.models.user import User


class AdminDBService(BaseDBService):
    def __init__(self, msg: Message):
        super().__init__(msg)

    async def get_users(self) -> tuple[User]:
        async with self.session() as session:
            result = await session.execute(select(User))
            users = result.first()
        return users
