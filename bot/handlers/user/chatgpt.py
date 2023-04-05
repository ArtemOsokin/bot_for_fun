from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from bot.handlers.other import ChatWorkStates
from bot.services.chatgpt import ChatGPT
from bot.misc.conf import Settings as set


async def start_chat_completion(msg: Message, state: FSMContext):
    await state.set_state(ChatWorkStates.chat_on)
    await msg.answer('Можешь приступать к своим волшебным запросам!')
    await msg.answer('Как надумаешь закончить, введи команду:\n/stop_chat')


async def stop_chat_completion(msg: Message, state: FSMContext):
    await state.reset_state()
    await msg.answer('Заявки на запросы больше не принимаются =) GL HF ')


async def chat_completion(msg: Message):
    if msg.text.startswith('/'):
        return await msg.answer('Нужен запрос к чату, а не команда!'
                                '... Четкий и понятный! Повтори')
    await msg.answer('Запрос отправлен! Ждём ответа...')
    await msg.answer('Жмякать никуда не надо! Просто подожди :3')

    response = ChatGPT(set.OPENAPI_KEY, set.OPENAPI_ORG).chat_completions(msg.text)
    await msg.answer(response)
    await msg.answer("*** REPONSE FROM CHATGPT ***")
