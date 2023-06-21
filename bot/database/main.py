from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from bot.misc.conf import settings


def create_engine(db_uri: str) -> AsyncEngine:
    echo = True if not settings.DEBUG else False
    return create_async_engine(db_uri, echo=echo, future=True)


async def proceed_schemas(engine: AsyncEngine, metadata) -> None:
    async with engine.begin() as conn:
        if not settings.DEBUG:
            await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> async_sessionmaker:
    return async_sessionmaker(engine, expire_on_commit=False, future=True)
