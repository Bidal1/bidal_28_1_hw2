from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINS
from aiogram.dispatcher import FSMContext


class fsmAdminMentor(StatesGroup):
    ID = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer('Вы не админ !')
    else:
        await fsmAdminMentor.ID.set()
        await message.answer(' ID ментора ? ')


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMContext_PROXY_STORAGE:
        FSMContext_PROXY_STORAGE['ID'] = message.text
    await fsmAdminMentor.next()
    await message.answer('Имя ?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMContext_PROXY_STORAGE:
        FSMContext_PROXY_STORAGE['name'] = message.text
    await fsmAdminMentor.next()
    await message.answer('Направление ?')


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMContext_PROXY_STORAGE:
        FSMContext_PROXY_STORAGE['direction'] = message.text
    await fsmAdminMentor.next()
    await message.answer('Возраст ?')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMContext_PROXY_STORAGE:
        FSMContext_PROXY_STORAGE['age'] = message.text
    await fsmAdminMentor.next()
    await message.answer('Группа ?')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMContext_PROXY_STORAGE:
        FSMContext_PROXY_STORAGE['group'] = message.text
    await fsmAdminMentor.next()
    await message.answer(f"Информация о менторе ?\n"
                         f"ID - {FSMContext_PROXY_STORAGE['ID']}\n"
                         f"Имя - {FSMContext_PROXY_STORAGE['name']}\n"
                         f"Направление - {FSMContext_PROXY_STORAGE['direction']}\n"
                         f"Возраст - {FSMContext_PROXY_STORAGE['age']}\n"
                         f"Группа - {FSMContext_PROXY_STORAGE['group']}\n")
    await message.answer('Верно ли ?')


async def load_sumbit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        await message.answer('готово')
        await state.finish()
    elif message.text == 'нет':
        await message.answer('хорошо')
        await state.finish()


def register_mentor(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg']),
    dp.register_message_handler(load_id, state=fsmAdminMentor.ID),
    dp.register_message_handler(load_name, state=fsmAdminMentor.name),
    dp.register_message_handler(load_direction, state=fsmAdminMentor.direction),
    dp.register_message_handler(load_age, state=fsmAdminMentor.age),
    dp.register_message_handler(load_group, state=fsmAdminMentor.group),
    dp.register_message_handler(load_sumbit, state=fsmAdminMentor.submit),
