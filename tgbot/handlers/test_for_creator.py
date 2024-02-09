from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.dispatcher import FSMContext

from tgbot.misc.states import Test_state
from tgbot.keyboards.all_inlinekeyboard import Inner_board
from tgbot.keyboards.all_replykeyboard import Reply_board


async def func1(message: Message):
    print("Hi1")
    await message.answer("Hi1", reply_markup=Inner_board.inline_for_sto("First", "Second"))
    await Test_state.st1.set()


async def func2(call: CallbackQuery, state: FSMContext):
    print("Hi2")
    await call.message.answer(text="Hi2", reply_markup=Reply_board().replay_keyboard("test1", "test2"))
    # await call.message.answer(text="Hi2", reply_markup=Inner_board.inline_for_sto("test1", "test2"))
    await Test_state.st2.set()


async def func3(call: CallbackQuery, state: FSMContext):
    print("Hi3")
    print(call.as_json())
    await call.message.answer(f"Hi3 and {call.data}")
    await state.finish()


# async def func3(message: Message, state: FSMContext):
#     print("Hi3")
#     print(message.as_json())
#     await message.answer("Hi3")
#     await state.finish()


def register_test_command(dp: Dispatcher):
    dp.register_message_handler(func1, commands="test")
    dp.register_callback_query_handler(func2, state=Test_state.st1)
    dp.register_callback_query_handler(func3, state=Test_state.st2)
    # dp.register_message_handler(func3, state=Test_state.st2)
