from aiogram import Bot, Dispatcher, types
from config import dp
from aiogram.utils import executor
from decouple import config
from handlers import callback, client, admin, extra, FSMAdminMentor
import logging

TOKEN = config('BOT_TOKEN')
FSMAdminMentor.register_mentor(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, )
