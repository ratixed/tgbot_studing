from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token='5240411060:AAEaduj76W3rqZAIa2XlFEBu1d5a-x5tkSg')
dp = Dispatcher(bot, storage=storage)

