from aiogram import Dispatcher
from aiogram.types import Message


async def func_support(message: Message):
    await message.answer("Контакти техпідтримки:📶")
    await message.answer_contact("+12345678", "John", "Smith")
    await message.answer_contact("+98765432", "Sherlock", "Holmes")
    await message.answer("Творець @Trecker007")
# , якщо є побажання або зауваження, можете писати йому!

def register_support(dp: Dispatcher):
    dp.register_message_handler(func_support, commands="support", state="*")
