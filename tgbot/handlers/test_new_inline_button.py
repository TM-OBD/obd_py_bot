from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.all_inlinekeyboard import Inner_board


async def test_func1(message: Message):
    await message.answer("text1", reply_markup=Inner_board.test_inlines()[0])


async def test_func2(call: CallbackQuery):
    await call.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                             reply_markup=Inner_board.test_inlines()[1])


async def test_func3(call: CallbackQuery):
    await call.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                             reply_markup=Inner_board.test_inlines()[0])


def register_test_inlines(dp: Dispatcher):
    dp.register_message_handler(test_func1, commands="test")
    dp.register_callback_query_handler(test_func2, text=["test1", "test2"])
    dp.register_callback_query_handler(test_func3, text="back")