from aiogram.utils import executor
from create_bot import dp
from handlers import client, other


async def on_startup(_):
    print('Бот вышел в онлайн')


client.register_handlers_client()
other.register_handlers_client()

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
