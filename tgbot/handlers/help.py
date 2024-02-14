from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.all_replykeyboard import Reply_board


async def func_help(message: Message):
    await message.answer("<b>Список основних команд:❔\n/status\n/services\n/info</b>",
                         reply_markup=Reply_board(input_field_placeholder="Choose or no ",
                                                  one_time_keyboard=True).replay_keyboard(
                             "Додаткові команди"))


# ❔

async def func_support_help(message: Message):
    await message.answer("Додаткові команди:❔\n/id\n/support")


def register_help(dp: Dispatcher):
    dp.register_message_handler(func_help, commands="help", state="*")
    dp.register_message_handler(func_support_help, text="Додаткові команди")
