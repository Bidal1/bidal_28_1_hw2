from aiogram import Bot, Dispatcher
from decouple import config


TOKEN = config('BOT_TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
ADMINS = (1064853961,)