from aiogram import Dispatcher

from bot.filters.admin import IsAdmin
from bot.handlers.admin.users import check_users


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(check_users, IsAdmin(), commands=['check_users'])
