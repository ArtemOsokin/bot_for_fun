from aiogram.types import Message

from bot.database.methods.admin import AdminDBService


async def check_users(msg: Message):
    admin_db_service = AdminDBService(msg)
    users = await admin_db_service.get_users()
    answer = '\n'.join(
        [
            f'{user.tg_id}: {user.username} {user.first_name} {user.last_name} - {user.gpt_count_requests} GPT запросов'
            for user in users
        ]
    )
    await msg.answer(answer)
