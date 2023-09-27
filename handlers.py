import glob
import os
from aiogram import Router
from aiogram.types import Message, input_file
from aiogram.filters.command import Command
from aiogram import types



from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
router = Router(name=__name__)

# Работа с FSM (конечным автоматом)


class ChoosingOrder(state.StatesGroup):
    choosing_order = state.State()


@router.message(Command('find'))
async def cmd_find(message: Message, state: FSMContext):
    await message.answer(text='Напишите номер заказа:')
    await state.set_state(ChoosingOrder.choosing_order)




@router.message(
    ChoosingOrder.choosing_order
)
async def order_chosen(message: Message, state: FSMContext):
    global flag
    await state.update_data(chosen_order=int(message.text))
    num_of_order = (await state.get_data())['chosen_order']

    await message.answer(text=f'Секундочку... Ищу заказ {num_of_order}!')
    flag = False
    for filename in glob.iglob('/users/egormakarov/desktop/test1/**', recursive=True):
        if os.path.isfile(filename):
            if filename[filename.rfind('/') + 1:] == f'{num_of_order}.pdf':
                global path_to_order
                path_to_order = str(f'{filename}')
                flag = True
                break
    if flag:
        doc = input_file.FSInputFile(path=rf'{path_to_order}')
        result = await message.answer_document(doc)
    else:
        await message.answer(f'Заказ {num_of_order} не найден...')


@router.message(Command('help'))
async def message_handler(message: Message):
    await message.answer('I`m gonna help you!')





