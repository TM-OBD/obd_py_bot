from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.all_replykeyboard import Reply_board


async def func_help(message: Message):
    await message.answer("Список основных комманд:\n/status\n???\n???",
                         reply_markup=Reply_board(input_field_placeholder="Choose or no ", one_time_keyboard=True).replay_keyboard(
                             "Дополнительные команды"))


async def func_support_help(message: Message):
    await message.answer("Additional commands:\n/id\n/support\n???")


def register_help(dp: Dispatcher):
    dp.register_message_handler(func_help, commands="help")
    dp.register_message_handler(func_support_help, text="Дополнительные команды")
