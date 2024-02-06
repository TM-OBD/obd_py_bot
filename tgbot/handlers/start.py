from aiogram import Dispatcher
from aiogram.types import Message
# from aiogram.types import CallbackQuery
# from tgbot.handlers.help import func_help

# from temporary import Temp_test
from tgbot.keyboards.all_replykeyboard import Reply_board
from tgbot.handlers.help import func_help


async def user_start(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=Reply_board(one_time_keyboard=True).replay_keyboard("/help"))
    await func_help(message)


# async def user_call(message: Message):
#     await message.answer(func_help(message))


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    # dp.register_callback_query_handler(user_call, text="help")
