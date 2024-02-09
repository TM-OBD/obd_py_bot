from aiogram.types import Message
from aiogram import Dispatcher


async def func_id(message: Message):
    await message.answer(f"Ваш індифікатор(id): {message.from_user.id}")


def register_id(dp: Dispatcher):
    dp.register_message_handler(func_id, commands="id")
