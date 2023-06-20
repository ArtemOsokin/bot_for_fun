from abc import ABC

from aiogram.types import Message


class BaseDBService(ABC):
    def __init__(self, msg: Message):
        self.session = msg.bot.get('session')
