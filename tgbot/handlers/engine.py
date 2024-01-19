from aiogram import Dispatcher
from aiogram.types import Message


async def engine_degree(message: Message):
    degree: str = "Неизвестно"
    if degree == "Неизвестно":
        await message.answer("Houston, we've got a problem.")
    await message.answer(f"Текущая температура в C:{degree} и F:{degree}")


def register_engine_degree(dp: Dispatcher):
    dp.register_message_handler(engine_degree, commands="engine_degree")
