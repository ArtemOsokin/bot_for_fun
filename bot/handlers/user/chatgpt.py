from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import BotCommandScopeDefault, Message

from bot.handlers.commands import get_chatgpt_on_commands, get_start_commands
from bot.handlers.other import ChatWorkStates
from bot.misc.conf import settings as set
from bot.services.chatgpt import ChatGPT


async def start_chat_completion(msg: Message, state: FSMContext):
    """
    Хендлер активации "режима" отправки запросов в ChatGPT
    :param msg: объект Message
    :param state: объект FSMContext
    :return:
    """

    await state.set_state(ChatWorkStates.chat_on)
    await msg.bot.set_my_commands(get_chatgpt_on_commands())
    await msg.answer('Можешь приступать к своим волшебным запросам!')
    await msg.answer('Как надумаешь закончить, введи команду:\n/stop_chat')


async def stop_chat_completion(msg: Message, state: FSMContext):
    """
    Хендлер остановки "режима" отправки запросов в ChatGPT

    :param msg: объект Message
    :param state: объект FSMContext
    :return:
    """

    await state.finish()
    await msg.bot.set_my_commands(get_start_commands())
    await msg.answer('Заявки на запросы больше не принимаются =) GL HF ')


async def chat_completion(msg: Message):
    """
    Хендлер отправки запросов в ChatGPT

    :param msg: объект Message
    :return:
    """

    if msg.text.startswith('/'):
        return await msg.answer(
            'Нужен запрос к чату, а не команда!' '... Четкий и понятный! Повтори'
        )
    await msg.answer('Запрос отправлен! Ждём ответа...')
    await msg.answer('Жмякать никуда не надо! Просто подожди :3')

    # todo: uncomment ChatGPT
    chat_gpt_service = ChatGPT(set.OPENAPI_KEY, set.OPENAPI_ORG)

    response = await chat_gpt_service.chat_completions(msg.text)

    await msg.answer(response)
    await msg.answer("*** END RESPONSE FROM CHATGPT ***")


def register_chatgpt_handlers(dp: Dispatcher) -> None:
    """
    Регистрирует хендлеры для работы с ChatGPT
    :param dp: объект Dispatcher
    :return: None
    """

    dp.register_message_handler(start_chat_completion, commands=['start_chat'])
    dp.register_message_handler(
        stop_chat_completion, state=ChatWorkStates.chat_on, commands=['stop_chat']
    )
    dp.register_message_handler(chat_completion, state=ChatWorkStates.chat_on)
