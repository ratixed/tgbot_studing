from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher.filters import Text
from generators.quote import Generate


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# Начало диалога загрузки нового пункта меню
async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузи фото')


# Ловим первый ответ и пишем его в словарь
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Теперь введи название')


# Ловим второй ответ
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введи описание')


# Ловим третий ответ
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Введи цену')


# Ловим последний ответ и используем полученные данные
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


# Выход из состояний
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


# Генерация цитаты
async def quote_generate(message: types.Message):
    await message.delete()
    await message.answer(Generate.quote())


# Регистрируем хендлеры
def register_handlers_admin():
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(quote_generate, Text(equals='💬 Генератор цитат', ignore_case=True), state='*')
