from aiogram import Dispatcher

from bot.handlers.admin import register_admin_handlers
from bot.handlers.other import register_other_handlers
from bot.handlers.user import register_user_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    """
    Регистрация всех хендлеров
    :param dp: объект Dispatcher
    :return:
    """

    handlers = (
        register_other_handlers,
        register_user_handlers,
        register_admin_handlers,
    )
    for handler in handlers:
        handler(dp)
