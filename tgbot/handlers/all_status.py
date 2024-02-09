from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.all_inlinekeyboard import Inner_board


# async def all_status(message: Message):
#     await message.answer("Текущий статус машины:\n\nМестоположение - неизвестно"
#                          "\nОбщие состояние машины - неизвестно\nПоломки - неизвестно\nПредупреждения - неизвестно\nЗаряд аккумулятора - неизвестно")
#     await asyncio.sleep(4)
#     anim = await message.answer_animation("CgACAgIAAxkBAAIBOWW4AAF4wzRV8Zx8hq6fhEvYtiTz7gACsgsAAlfVEEn18wijZMbfqDQE")
#     await asyncio.sleep(2.5)
#     await message.bot.delete_message(message.chat.id, anim.message_id)

async def all_status1(message: Message):
    await message.answer("<code>Выберете машину:</code>", reply_markup=Inner_board.status_inlines()[0])


async def all_status2(call: CallbackQuery):
    await call.bot.edit_message_text("<b>Текущий статус машины:</b>\n\n"
                                     "<i>Заряд аккумулятора:</i> неизвестно❓\n<i>Уровень масла:</i> неизвестно❓\n<i>Местоположение:</i> неизвестно❓\n<i>Поломоки:</i> нет✅",
    # <a href='https://www.isyb.com.ua/'>Company</a>
                                     call.message.chat.id, call.message.message_id,
                                     reply_markup=Inner_board.status_inlines()[1])


async def all_status3(call: CallbackQuery):
    await call.bot.edit_message_text("Выберете машину:", call.message.chat.id, call.message.message_id, reply_markup=Inner_board.status_inlines()[0])


def register_all_status(dp: Dispatcher):
    dp.register_message_handler(all_status1, commands="status")
    dp.register_callback_query_handler(all_status2, text=["car1", "car2"])
    dp.register_callback_query_handler(all_status3, text="back")
