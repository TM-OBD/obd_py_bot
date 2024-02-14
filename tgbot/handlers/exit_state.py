from aiogram import Dispatcher
from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext

from tgbot.handlers.all_status import all_status1
from tgbot.handlers.help import func_help
from tgbot.handlers.id import func_id
from tgbot.handlers.service import serv_cto1
from tgbot.handlers.info import info
from tgbot.handlers.start import user_start1
from tgbot.handlers.support import func_support


# async def echo(message: Message):
#     await message.answer("<b>Я не зміг визначити команду спробуйте написати ще раз або натисніть команду /help, у ній описані всі доступні команди бота</b>")


# async def exit_st1(message: Message, state: FSMContext):
#     await state.finish()
#     if message.text == "/services":
#         await serv_cto1(message)
#     elif message.text == "/status":
#         await all_status1(message)
#     elif message.text == "/help":
#         await func_help(message)
#     elif message.text in ["/info", "Info"]:
#         await info(message)
#     elif message.text == "/start":
#         await user_start1(message)
#     elif message.text == "/support":
#         await func_support(message)
#     # elif message.text == "id":
    #     await func_id(message)


# def register_exit_state(dp: Dispatcher):
#     dp.register_message_handler(echo)
    # dp.register_message_handler(exit_st1, state="*", content_types=ContentTypes.ANY)

# await message.answer('Вы вышли из текущего состояния.')
# await message.answer('<span class="tg-spoiler">Вы вышли из текущего состояния.</span>')
# await message.answer("<pre>Вы вышли из текущего состояния.</pre>")
# await message.answer("<tg-spoiler>Вы вышли из текущего состояния.</tg-spoiler>")
