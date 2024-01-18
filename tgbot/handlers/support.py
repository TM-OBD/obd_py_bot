from aiogram import Dispatcher
from aiogram.types import Message

async def func_support(message: Message):
    await message.answer("Контакты:")
    await message.answer_contact("+12345678", "John", "Smith")
    await message.answer_contact("+98765432", "Holmes", "Sherlock")
    await message.answer("Creator and admin is @Trecker007")



def register_support(dp: Dispatcher):
    dp.register_message_handler(func_support, commands="support")