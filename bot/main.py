import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from bot.database.main import create_engine, get_session_maker, proceed_schemas
from bot.database.models.main import Base
from bot.filters import register_all_filters
from bot.handlers import register_all_handlers
from bot.misc import settings

engine = create_engine(settings.DB_URL)


async def __on_startup(dp: Dispatcher) -> None:
    await dp.bot.set_webhook(settings.WEBHOOK_URL)

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

    if settings.DEBUG:
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

    # создание экземпляра бота
    bot = Bot(token=settings.TOKEN, parse_mode='HTML')

    # создание seession_maker'a и передачи его
    # в data бота для дальнейшего использования при работе с БД
    session_maker = get_session_maker(engine)
    bot['session'] = session_maker

    # создание экземпляра диспетчера обновлений
    dp = Dispatcher(bot, storage=MemoryStorage())

    # создание вебхукинга
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=settings.WEBHOOK_PATH,
        on_startup=__on_startup,
        on_shutdown=__on_shutdown,
        skip_updates=True,
        host=settings.WEBAPP_HOST,
        port=settings.WEBAPP_PORT,
    )
