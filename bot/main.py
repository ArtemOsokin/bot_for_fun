import logging

from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.filters import register_all_filters
from bot.misc import Settings
from bot.handlers import register_all_handlers
from bot.database.main import create_engine, get_session_maker, proceed_schemas
from bot.database.models.main import Base

engine = create_engine(Settings.DB_URL)


async def __on_start_up(dp: Dispatcher) -> None:
    register_all_filters(dp)
    register_all_handlers(dp)

    await proceed_schemas(engine, Base.metadata)


def start_bot():
    if Settings.DEBUG:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

    bot = Bot(token=Settings.TOKEN, parse_mode='HTML')
    session_maker = get_session_maker(engine)
    bot['session'] = session_maker
    dp = Dispatcher(bot, storage=MemoryStorage())

    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
