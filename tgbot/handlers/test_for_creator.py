from aiogram import Dispatcher
from aiogram.types import Message, ContentType
# from aiogram.dispatcher import FSMContext

# from tgbot.misc.states import Test_state
from tgbot.keyboards.all_replykeyboard import Reply_board


async def func1(message: Message):
    await message.answer("Hi1",
                         reply_markup=Reply_board(request_location=True).replay_keyboard("Поделиться координатами"))


async def func2(message: Message):
    print("Yes")
    print(message)


def register_test_command(dp: Dispatcher):
    dp.register_message_handler(func1, commands="test", state="*")
    dp.register_message_handler(func2, content_types=ContentType.LOCATION)
