from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storege = MemoryStorage()
TOKEN = config('BOT_TOKEN')
Key = config('KEY')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storege)
ADMINS = (1064853961, )