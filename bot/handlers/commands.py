from typing import List

from aiogram.types import BotCommand


def get_start_commands() -> List[BotCommand]:
    return [
        BotCommand('start', 'Запуск/Перезапуск бота'),
        BotCommand('start_chat', 'Запуск режима отправки запросов в ChatGPT'),
        BotCommand('help', 'Список команд'),
        BotCommand('about', 'About'),
    ]


def get_chatgpt_on_commands() -> List[BotCommand]:
    return [
        BotCommand('stop_chat', 'Остановка режима отправки запросов в ChatGPT'),
    ]
