from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом, через лс, напишите ему.')


async def schedule(message: types.Message):
    await bot.send_message(message.from_user.id, 'Мы работаем для вас 24/7')


async def geolocation(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Сетевая 24.7', reply_markup=ReplyKeyboardRemove())


def register_handlers_client():
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(schedule, commands=['schedule'])
    dp.register_message_handler(geolocation, commands=['geolocation'])
