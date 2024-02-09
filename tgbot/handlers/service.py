from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from tgbot.filters.filter_сities import filter_cities_service
from tgbot.keyboards.all_replykeyboard import Reply_board
from tgbot.keyboards.all_inlinekeyboard import Inner_board
from tgbot.misc.states import State_cto


async def serv_cto1(message: Message, state: FSMContext):
    await message.answer("<code>Список ваших машин</code>",
                         reply_markup=Inner_board.inline_for_sto("Авто 1", "Авто 2"))
    await State_cto.st1.set()


async def serv_cto2(call: CallbackQuery, state: FSMContext):
    await call.bot.edit_message_text(text="<b>Оберіть послугу для вашого авто🔽</b>", chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     reply_markup=Inner_board.inline_for_sto("Шиномонтаж", "CTO"))
    await state.update_data(previous_state="State_cto.st2")
    await State_cto.st2.set()


async def serv_cto3(call: CallbackQuery, state: FSMContext):
    if call.data == "CTO":
        await call.bot.edit_message_text("<code>Ця команда перебуває у розробці</code>", chat_id=call.message.chat.id,
                                         message_id=call.message.message_id)
        await state.finish()
    else:
        await call.bot.edit_message_text(text="<b>Оберіть що вам потрібно🔽</b>", chat_id=call.message.chat.id,
                                         message_id=call.message.message_id,
                                         reply_markup=Inner_board.inline_for_sto("Сезонна заміна",
                                                                                 "Позапланове обслуговування"))
        await State_cto.st3.set()


async def serv_cto4(call: CallbackQuery, state: FSMContext):
    await state.update_data(data1=call.data)
    await call.message.answer(
        text="<b>Добре, виберіть місто обслуговування або напишіть самі🗺</b>",
        reply_markup=Reply_board(one_time_keyboard=True).replay_serv_city("Одесса", "Харків", "Київ",
                                                                          "Івано-Франківськ"))
    await State_cto.st4.set()


async def serv_cto4_5(message: Message, state: FSMContext):
    output = filter_cities_service(str(message.text))
    if not output:
        await message.answer(
            'Я не зміг впізнати введене місто, спробуйте ввести ще раз або оберіть потрібне місто у кнопках')
        return
    else:
        await serv_cto5(message, state)


async def serv_cto5(message: Message, state: FSMContext):
    city = filter_cities_service(str(message.text))
    await state.update_data(data2=city)
    await message.answer("<b>Виберете адресу шиномонтажу🗺</b>",
                         reply_markup=Inner_board.inline_for_sto("Адрес1", "Адрес2"))
    await State_cto.st5.set()


async def serv_cto6(call: CallbackQuery, state: FSMContext):
    await state.update_data(data3=call.data)
    await call.bot.edit_message_text("<b>Тепер оберіть дату и час 🕛 зі списку нижче🔽</b>", chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     reply_markup=Inner_board.inline_for_sto("08.02", "09.02", "10.2"))
    await State_cto.st6.set()


async def serv_cto7(call: CallbackQuery, state: FSMContext):
    await state.update_data(data4=call.data)
    if call.data == "08.02":
        await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                 message_id=call.message.message_id,
                                                 reply_markup=Inner_board.inline_for_sto("13:00", "14:00", "18:00",
                                                                                         "Повернутися до дат"))
    elif call.data == "09.02":
        await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                 message_id=call.message.message_id,
                                                 reply_markup=Inner_board.inline_for_sto("9:00", "10:00", "13:00"))
    elif call.data == "10.2":
        await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                 message_id=call.message.message_id,
                                                 reply_markup=Inner_board.inline_for_sto("10:00", "14:00", "15:00"))
    await State_cto.st7.set()


async def serv_cto8(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.bot.edit_message_text(chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     text="<b>Чудово, запит надіслано, менеджер відповість вам найближчим часом✅</b>"
                                          "\n<b>Введені дані:</b>\n\n<code>Послуга:</code> <b>{data1}</b>\n<code>Місто:</code> <b>{data2}</b> 🗺\n<code>Адрес:</code> <b>{data3} 🗺</b>\n<code>Дата:</code> {data4} 📅\n<code>Час:</code> <b>{data5} "
                                          "🕛</b>".format(
                                         data1=data.get("data1"), data2=data.get("data2"), data3=data.get("data3"),
                                         data4=data.get("data4"), data5=call.data))
    await state.finish()


def register_serv_cto(dp: Dispatcher):
    dp.register_message_handler(serv_cto1, commands="services")
    dp.register_callback_query_handler(serv_cto2, state=State_cto.st1)
    dp.register_callback_query_handler(serv_cto3, state=State_cto.st2)
    dp.register_callback_query_handler(serv_cto4, state=State_cto.st3)
    dp.register_message_handler(serv_cto4_5, state=State_cto.st4)
    dp.register_message_handler(serv_cto5, state=State_cto.st4)
    dp.register_callback_query_handler(serv_cto6, state=State_cto.st5)
    dp.register_callback_query_handler(serv_cto7, state=State_cto.st6, text=["08.02", "09.02", "10.2"])
    dp.register_callback_query_handler(serv_cto8, state=State_cto.st7)
