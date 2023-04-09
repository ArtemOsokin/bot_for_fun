from aiogram import Dispatcher, filters
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.database.methods import UserService
from bot.handlers.content import other


class ChatWorkStates(StatesGroup):
    chat_on = State()


async def start_cmd(msg: Message, state: FSMContext):
    await state.finish()

    user = await UserService(msg).get_user_by_tg_id()

    if not user:
        user = await UserService(msg).create_user()
        await msg.answer('\n'.join(
            [f'Приветствую, {user.first_name}!'] + other['start'])
        )
    else:
        await msg.answer('\n'.join(
            [f'С возвращением, {user.first_name}!'] + other['start'])
        )


async def help_cmd(msg: Message):
    await msg.answer('\n'.join(other['help']))


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start_cmd, filters.CommandStart())
    dp.register_message_handler(help_cmd, filters.CommandHelp())
