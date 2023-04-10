from aiogram import Dispatcher, filters
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.database.methods import UserService
from bot.handlers.content import answers
from bot.handlers.commands import get_start_commands


class ChatWorkStates(StatesGroup):
    chat_on = State()


async def start_cmd(msg: Message, state: FSMContext):
    """
    Хендлер для команды /start.
    Устанавливает меню команд с подсказками и добавляет пользователя
    в БД если его там нету

    :param msg: объект Message
    :param state: объект FSMContext
    :return:
    """

    await state.finish()
    await msg.bot.set_my_commands(get_start_commands())

    user = await UserService(msg).get_user_by_tg_id()

    if not user:
        user = await UserService(msg).create_user()
        await msg.answer('\n'.join(
            [f'Приветствую, {user.first_name}!'] + answers['start'])
        )
    else:
        await msg.answer('\n'.join(
            [f'С возвращением, {user.first_name}!'] + answers['start'])
        )


async def help_cmd(msg: Message):
    """
    Хендлер для команды /help
    :param msg: объект Message
    :return:
    """

    await msg.answer('\n'.join(answers['help']))


async def about_cmd(msg: Message):
    """
    Хендлер для команды /about
    :param msg: объект Message
    :return:
    """

    await msg.answer('\n'.join(answers['about']))


def register_other_handlers(dp: Dispatcher) -> None:
    """
    Регистрация прочих хэндлеров
    :param dp: объект Dispatcher
    :return:
    """

    dp.register_message_handler(start_cmd, filters.CommandStart())
    dp.register_message_handler(help_cmd, filters.CommandHelp())
    dp.register_message_handler(about_cmd, commands=['about'])
