from aiogram import Bot, Dispatcher, types
from config import dp, ADMINS
from aiogram.utils import executor
from decouple import config
from handlers import callback, client, admin, extra, FSMAdminMentor
import logging
import asyncio
from database.bot_dp import sql_create, register_message_Bot_db
from config import bot


async def on_startup(_):
    await bot.send_message(chat_id=ADMINS[0], text="Бот запущен!")
    sql_create()


FSMAdminMentor.register_mentor(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
register_message_Bot_db(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
