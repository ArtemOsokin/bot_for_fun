from aiogram.types import Message

from bot.database.methods.admin import AdminDBService


async def check_users(msg: Message):
    admin_db_service = AdminDBService(msg)
    users = await admin_db_service.get_users()
    print(users)
    answer = '\n'.join(
        [f'{user.tg_id}: {user.username} {user.first_name} {user.last_name}' for user in users]
    )
    await msg.answer(answer)