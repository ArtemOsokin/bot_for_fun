from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from bot.misc import settings


class IsAdmin(BoundFilter):
    async def check(self, msg: Message) -> bool:
        if msg.from_user.id in settings.ADMINS:
            return True
        return False
