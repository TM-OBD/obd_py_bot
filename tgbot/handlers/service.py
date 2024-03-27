from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from tgbot.filters.filter_сities import filter_cities_service
from tgbot.keyboards.all_replykeyboard import Reply_board
from tgbot.keyboards.all_inlinekeyboard import Inner_board
from tgbot.misc.states import State_cto
from tgbot.services.fresh_requests import FreshServiceRequests


async def serv_cto1(message: Message):
    await message.answer("<code>Оберіть авто для обслуговування</code>",
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
        await state.update_data(current_state="serv_cto3")
        await call.bot.edit_message_text(text="<b>Оберіть що вам потрібно🔽</b>", chat_id=call.message.chat.id,
                                         message_id=call.message.message_id,
                                         reply_markup=Inner_board.inline_for_sto("Сезонна заміна",
                                                                                 "Позапланове обслуговування"))
        await State_cto.st3.set()


async def serv_cto4(call: CallbackQuery, state: FSMContext):
    previous_state = (await state.get_data()).get("current_state")
    if previous_state == "serv_cto3":
        await state.update_data(data1=call.data, current_state="serv_cto4")
    await call.message.answer(
        text="<b>Добре, виберіть місто обслуговування або напишіть самі🗺</b>",
        reply_markup=Reply_board(one_time_keyboard=True).replay_serv_city("Одесса", "Харків", "Київ",
                                                                          "Івано-Франківськ"))
    await State_cto.st4.set()


async def serv_cto4_5(message: Message, state: FSMContext):
    # print(f"serv_cto 4_5: {message}")
    # await state.update_data(current_state="serv_cto4_5")
    output = filter_cities_service(str(message.text))
    if not output:
        print(message)
        await message.answer(
            'Я не зміг впізнати введене місто, спробуйте ввести ще раз або оберіть потрібне місто у кнопках')
        return
    else:
        await message.reply(f"Місто {output}?", reply_markup=Inner_board.inline_for_sto("Так", "Ні"))


async def serv_cto_4_5_yes_no(call: CallbackQuery, state: FSMContext):
    # print(f"serv_cto 4_5_y_n: {call.message.text}")
    if call.data == "Так":
        await serv_cto5(call.message, state)
    else:
        # previous_state = (await state.get_data()).get("current_state")
        # if previous_state == "serv_cto4_5":
        # data = await state.get_data()
        await state.update_data(current_state="serv_y_n")
        await serv_cto4(call, state)
        # await state.update_data(**data)
    # else:
    #     await serv_cto4(call, state)


async def serv_cto5(message: Message, state: FSMContext):
    await message.delete()
    previous_state = (await state.get_data()).get("current_state")
    if previous_state in ["serv_cto4", "serv_y_n"]:
        text = message.text.split()[1][:-1]
        # print(f"serv_cto 5: {text}")
        city = filter_cities_service(str(text))
        await state.update_data(data2=city, current_state="serv_cto5")

    await message.answer("<b>Виберете адресу шиномонтажу🗺</b>",
                         reply_markup=Inner_board.inline_for_sto("Адрес1", "Адрес2", "Повернутися до вибору міста"))
    await State_cto.st5.set()


async def serv_back_in_4(call: CallbackQuery, state: FSMContext):
    previous_state = (await state.get_data()).get("current_state")
    if previous_state == "serv_cto5":
        data = await state.get_data()
        await serv_cto4(call, state)
        await state.update_data(**data)


# async def serv_cto6(call: CallbackQuery, state: FSMContext):
#     # print(f"serv_cto 6: {call.data}")
#     await state.update_data(data3=call.data, current_state="serv_cto6")
#     await call.bot.edit_message_text("<b>Тепер оберіть дату и час 🕛 зі списку нижче🔽</b>", chat_id=call.message.chat.id,
#                                      message_id=call.message.message_id,
#                                      reply_markup=Inner_board.inline_for_sto("08.02", "09.02", "10.2",
#                                                                              "Повернутися до вибору адреси"))
#     await State_cto.st6.set()


# async def serv_back_in_5(call: CallbackQuery, state: FSMContext):
#     previous_state = (await state.get_data()).get("current_state")
#     if previous_state == "serv_cto6":
#         data = await state.get_data()
#         await serv_cto5(call.message, state)
#         await state.update_data(**data)


# async def serv_cto7(call: CallbackQuery, state: FSMContext):
#     await state.update_data(data4=call.data, current_state="serv_cto7")
#     if call.data == "08.02":
#         await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,
#                                                  message_id=call.message.message_id,
#                                                  reply_markup=Inner_board.inline_for_sto("13:00", "14:00", "18:00",
#                                                                                          "Повернутися до дат"))
#     elif call.data == "09.02":
#         await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,
#                                                  message_id=call.message.message_id,
#                                                  reply_markup=Inner_board.inline_for_sto("9:00", "10:00", "13:00",
#                                                                                          "Повернутися до дат"))
#     elif call.data == "10.2":
#         await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,
#                                                  message_id=call.message.message_id,
#                                                  reply_markup=Inner_board.inline_for_sto("10:00", "14:00", "15:00",
#                                                                                          "Повернутися до дат"))
#     await State_cto.st7.set()


# async def serv_back_in_6(call: CallbackQuery, state: FSMContext):
#     previous_state = (await state.get_data()).get("current_state")
#     if previous_state == "serv_cto7":
#         data = await state.get_data()
#         await serv_cto6(call, state)
#         await state.update_data(**data)
async def last_question(call: CallbackQuery, state: FSMContext):
    # print("last_question")
    await call.message.delete()
    data = await state.get_data()
    # await state.update_data(data3=call.data)
    await call.bot.send_message(call.message.chat.id, "Запит буде надіслано, ви впевнені?"
                                                      "\n<b>Введені дані:</b>\n\n<code>Послуга:</code> <b>{data1}</b>\n<code>Місто:</code> <b>{data2}</b> 🗺\n<code>Адрес:</code> <b>{data3} 🗺</b>".format(
        data1=data.get("data1"), data2=data.get("data2"), data3=call.data),
                                reply_markup=Inner_board.inline_for_sto("Так!", "Повернутися назад"))
    await State_cto.st6.set()


async def between_two_fires(call: CallbackQuery, state: FSMContext):
    # print("between_two_fires")
    if call.data == "Так!":
        await serv_cto8(call, state)
    else:
        data = await state.get_data()
        await serv_cto5(call.message, state)
        await state.update_data(**data)


async def serv_cto8(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()

    await call.message.answer(text="<b>Чудово, запит надіслано, менеджер відповість вам найближчим часом✅</b>"
                                   "\n<b>Введені дані:</b>\n\n<code>Послуга:</code> <b>{data1}</b>\n<code>Місто:</code> <b>{data2}</b> 🗺\n<code>Адрес:</code> <b>{data3} 🗺</b>".format(
        data1=data.get("data1"), data2=data.get("data2"), data3=call.message.text.split()[-2]),
        reply_markup=ReplyKeyboardRemove())
    subject = data.get("data1")
    description = f"City: {data.get('data2')}, Address: {call.message.text.split()[-2]}"
    c = FreshServiceRequests()
    c.create_ticket(subject=subject, description=description)
    await state.finish()


def register_serv_cto(dp: Dispatcher):
    dp.register_message_handler(serv_cto1, commands="services", state="*")
    dp.register_callback_query_handler(serv_cto2, state=State_cto.st1)
    dp.register_callback_query_handler(serv_cto3, state=State_cto.st2)
    dp.register_callback_query_handler(serv_cto4, state=State_cto.st3)
    dp.register_message_handler(serv_cto4_5, state=State_cto.st4)
    dp.register_callback_query_handler(serv_cto_4_5_yes_no, state=State_cto, text=["Так", "Ні"])
    dp.register_message_handler(serv_cto5, state=State_cto.st4)
    dp.register_callback_query_handler(serv_back_in_4, state=State_cto, text="Повернутися до вибору міста")
    # dp.register_callback_query_handler(serv_cto6, state=State_cto.st5)
    # dp.register_callback_query_handler(serv_back_in_5, state=State_cto, text="Повернутися до вибору адреси")
    # dp.register_callback_query_handler(serv_cto7, state=State_cto.st6, text=["08.02", "09.02", "10.2"])
    # dp.register_callback_query_handler(serv_back_in_6, state=State_cto, text="Повернутися до дат")
    dp.register_callback_query_handler(last_question, state=State_cto.st5)
    dp.register_callback_query_handler(between_two_fires, state=State_cto, text=["Так", "Повернутися назад"])
    dp.register_callback_query_handler(serv_cto8, state=State_cto.st6)
