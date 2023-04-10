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


async def __on_startup(dp: Dispatcher) -> None:
    await dp.bot.set_webhook(Settings.WEBHOOK_URL)

    register_all_filters(dp)
    register_all_handlers(dp)

    await proceed_schemas(engine, Base.metadata)


async def __on_shutdown(dp: Dispatcher) -> None:

    await dp.bot.delete_webhook()

    await dp.storage.close()
    await dp.storage.wait_closed()


def start_bot():
    """
    Запуск бота в режиме Webhook

    :return:
    """

    if Settings.DEBUG:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

    # создание экземпляра бота
    bot = Bot(token=Settings.TOKEN, parse_mode='HTML')

    # создание seession_maker'a и передачи его
    # в data бота для дальнейшего использования при работе с БД
    session_maker = get_session_maker(engine)
    bot['session'] = session_maker

    # создание экземпляра диспетчера обновлений
    dp = Dispatcher(bot, storage=MemoryStorage())

    # создание вебхукинга
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=Settings.WEBHOOK_PATH,
        on_startup=__on_startup,
        on_shutdown=__on_shutdown,
        skip_updates=True,
        host=Settings.WEBAPP_HOST,
        port=Settings.WEBAPP_PORT,
    )
