from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

# from temporary import Temp_test
from tgbot.keyboards.all_inlinekeyboard import Inner_board
from tgbot.misc.states import State_cto


async def serv_cto1(message: Message):
    await message.answer("Хорошо, выберете нужный запрос",
                         reply_markup=Inner_board.inline_for_sto("Поменять на летнюю резину",
                                                                 "Поменять на зимнюю резину",
                                                                 "Отправить другой запрос"))
    await State_cto.st1.set()


async def serv_cto2(call: CallbackQuery, state: FSMContext):
    await call.bot.edit_message_text(text="Отлично, выберете город", chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     reply_markup=Inner_board.inline_for_sto("Одесса", "Харьков", "Киев", "Донецк",
                                                                             "Ивано-Франковск", "Черновцы", "back"))
    await State_cto.st2.set()


async def serv_cto3(call: CallbackQuery, state: FSMContext):
    await call.bot.edit_message_text(text="Выберете адрес СТО", chat_id=call.message.chat.id,
                                     message_id=call.message.message_id,
                                     reply_markup=Inner_board.inline_for_sto("Адрес 1", "Адрес 2", "Адрес 3", "back"))
    await State_cto.st3.set()


async def serv_cto4(call: CallbackQuery, state: FSMContext):
    await call.bot.edit_message_text(
        text="Теперь, напишите желаемое время.Пример: Июнь 4-5, время 12:00, 13:00, 18:00",
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        reply_markup=Inner_board.inline_for_sto("back"))
    await State_cto.st4.set()


async def serv_cto5(message: Message, state: FSMContext):
    await message.answer(text="Отлично, запрос отправлен, менеджер ответит вам в ближайшее время")
    await state.finish()


def register_serv_cto(dp: Dispatcher):
    dp.register_message_handler(serv_cto1, commands="cto")
    dp.register_callback_query_handler(serv_cto2, text=["Поменять на летнюю резину", "Поменять на зимнюю резину",
                                                        "Отправить другой запрос"], state=State_cto.st1)
    dp.register_callback_query_handler(serv_cto3,
                                       text=["Одесса", "Харьков", "Киев", "Донецк", "Ивано-Франковск", "Черновцы"],
                                       state=State_cto.st2)
    dp.register_callback_query_handler(serv_cto4, text=["Адрес 1", "Адрес 2", "Адрес 3"], state=State_cto.st3)
    dp.register_message_handler(serv_cto5, state=State_cto.st4)
    # dp.register_callback_query_handler(serv_cto5, text="Теперь, напишите желаемое время.Например: Июнь 4-5, время 12:00, 13:00, 18:00",
    #                                    state=State_cto.st4)
