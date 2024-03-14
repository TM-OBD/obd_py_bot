from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    await message.reply("Hello, admin!")
    await message.answer("Admin commands:\n/admins_help\n???\n???\n???")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["help_admin"], state="*", is_admin=True)
