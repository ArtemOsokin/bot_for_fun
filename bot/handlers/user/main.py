from aiogram import Dispatcher

from bot.handlers.user.chatgpt import register_chatgpt_handlers


def register_user_handlers(dp: Dispatcher):
    register_chatgpt_handlers(dp)

