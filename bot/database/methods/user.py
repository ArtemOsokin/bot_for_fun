from aiogram import types
from sqlalchemy import select

from bot.database.models.user import User


class UserService:
    def __init__(self, msg: types.Message) -> None:
        """
        :param msg: объект Message телеграмм
        """
        self.msg = msg

    async def create_user(self) -> User:
        """
        Создаёт пользователя в базе данных
        :return None:
        """
        user = User(
            tg_id=self.msg.from_user.id,
            first_name=self.msg.from_user.first_name,
            last_name=self.msg.from_user.last_name,
            username=self.msg.from_user.username
        )

        session = self.msg.bot.get('session')

        async with session() as session:
            async with session.begin():
                session.add(user)
                try:
                    await session.commit()
                except Exception:
                    await session.rollback()
        return user

    async def get_user_by_tg_id(self) -> User | None:
        """
        Возвращает пользователя по Юзер ИД Телеграмма

        :return None|User:

        >>> get_user_by_tg_id(123)
        User(id=1, tg_id=123, first_name='John, last_name='Doe', ...)
        """

        stmt = select(User).where(User.tg_id==self.msg.from_user.id)

        session = self.msg.bot.get('session')

        async with session() as session:
            result = await session.execute(stmt)
            users = result.scalars()
            return users.first()
