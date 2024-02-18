from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove

from tgbot.keyboards.all_replykeyboard import Reply_board


async def func_help(message: Message):
    text = ("<b>Ви можете керувати мною, надіславши ці команди:</b>\n<b>Список основних команд:</b>❔\n\n"
            "/status - <b>Показує інформації про ваші машини від obd</b>\n/services - <b>Надіслати запит на сервіс</b>\n/info - <b>Інформація про продукт</b>")

    await message.answer(text, reply_markup=Reply_board(input_field_placeholder="Choose or no ",
                                                        one_time_keyboard=True).replay_keyboard(
        "Додаткові команди"))


async def func_support_help(message: Message):
    await message.answer("Додаткові команди:❔\n/id - Ваш id телеграмма\n/support - Контакти техпідтримки", reply_markup=ReplyKeyboardRemove())


def register_help(dp: Dispatcher):
    dp.register_message_handler(func_help, commands="help", state="*")
    dp.register_message_handler(func_support_help, text="Додаткові команди", state="*")

#status-Інформація про ваші машини
#services-Послуги сервісів
#info-Інформація про продукт
#help-Детальний опис команд бота
