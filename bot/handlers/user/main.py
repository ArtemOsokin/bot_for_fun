from aiogram import Dispatcher

from bot.handlers.user.chatgpt import (
    start_chat_completion,
    stop_chat_completion,
    chat_completion
)
from bot.handlers.other import ChatWorkStates


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_chat_completion,
        state=ChatWorkStates.chat_off,
        commands=['start_chat']
    )
    dp.register_message_handler(
        stop_chat_completion,
        state=ChatWorkStates.chat_on,
        commands=['stop_chat']
    )
    dp.register_message_handler(
        chat_completion,
        state=ChatWorkStates.chat_on
    )

