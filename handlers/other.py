from aiogram import types, Dispatcher
from generators.quote import Generate
from create_bot import dp, bot


async def quote_send(message: types.Message):
    await bot.send_message(message.from_user.id, Generate.quote())


def register_handlers_other():
    dp.register_message_handler(quote_send, commands=['quote'])