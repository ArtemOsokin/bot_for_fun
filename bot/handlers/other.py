from aiogram import Dispatcher, filters
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters.state import StatesGroup, State


class ChatWorkStates(StatesGroup):
    chat_on = State()
    chat_off = State()


async def start_cmd(msg: Message, state: FSMContext):
    await state.set_state(ChatWorkStates.chat_off)
    text_list = [
        f'Приветствую, {msg.from_user.full_name}!',
        'Для включения режима ChatGPT введи команду: /start_chat',
        'Как только закончишь - не забудь отправить: /stop_chat',
        'Удачи, Друг! 🪬'
    ]
    text = '\n'.join(text_list)
    await msg.answer(text)


async def help_cmd(msg: Message):
    help_list = [
        '/start - запуск бота',
        '/start_chat - включить режим ChatGPT',
        '/stop_chat - выключить ChatGPT (только с включенным режимом)',
        '/help - список команд',
        '🪬'
    ]
    help_text = '\n'.join(help_list)
    await msg.answer(help_text)


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start_cmd, filters.CommandStart())
    dp.register_message_handler(help_cmd, filters.CommandHelp())
