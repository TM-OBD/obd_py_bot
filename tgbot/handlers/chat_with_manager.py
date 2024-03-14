from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from tgbot.keyboards.all_inlinekeyboard import Inner_board


async def chat1(message: Message):
    await message.answer("При создании чата с менеджером, вы не сможете пользоваться другими командами, вы уверены что хотить создать чат с менеджером?",
                         reply_markup=Inner_board.chat_with_manager1())


async def chat_deny(call: CallbackQuery):
    await call.message.answer("Good")


async def chat2(call: CallbackQuery):
    await call.message.answer("Чат создан, для выхода из состаяния чата нажмите кнопку - выйти")


async def exit_chat(call: CallbackQuery):
    await call.message.answer("Вы выщли из состаяния чата☣")


def register_chat_with_manager(dp: Dispatcher):
    dp.register_message_handler(chat1, commands="chat_with_manager", state="*")
    dp.register_callback_query_handler(chat_deny, text="chat_no")
    dp.register_callback_query_handler(chat2, text="chat_yes")
    dp.register_callback_query_handler(exit_chat, text="exit_chat")
