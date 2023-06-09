import logging

from aiogram import types
from sqlalchemy import select

from bot.database.methods.base import BaseDBService
from bot.database.models.user import User


class UserDBService(BaseDBService):
    """
    Сервис для взаимодействия БД с данными пользователя
    """

    def __init__(self, msg: types.Message) -> None:
        """
        :param msg: объект Message телеграмм
        """

        super().__init__(msg)
        self.msg = msg
        self.tg_id = self.msg.from_user.id
        self.first_name = self.msg.from_user.first_name
        self.last_name = self.msg.from_user.last_name
        self.username = self.msg.from_user.username

    async def create_user(self) -> User:
        """
        Создаёт пользователя в базе данных
        :return User: объект пользователя
        """

        user = User(
            tg_id=self.tg_id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
        )

        async with self.session() as session:
            async with session.begin():
                session.add(user)
                try:
                    await session.commit()
                except Exception as e:
                    logging.error(e)
                    await session.rollback()
        return user

    async def get_user_by_tg_id(self) -> User | None:
        """
        Возвращает пользователя по Юзер ИД Телеграмма

        :return None | User: Объект пользователя

        >>> get_user_by_tg_id(123)
        User(id=1, tg_id=123, first_name='John, last_name='Doe', ...)
        """

        stmt = select(User).where(User.tg_id == self.tg_id)

        async with self.session() as session:
            result = await session.scalars(stmt)
            user = result.one_or_none()
        return user

    async def incr_gpt_count_req(self):
        """
        Увеличивает количество использованных запросов юзера на 1

        """

        stmt = select(User).where(User.tg_id == self.tg_id)

        async with self.session() as session:
            result = await session.scalars(stmt)
            user = result.one_or_none()
            print(user.gpt_count_requests)
            user.gpt_count_requests += 1
            print(user.gpt_count_requests)
            await session.flush()
            await session.commit()
        return user
