from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ContentTypes
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.all_inlinekeyboard import Inner_board
from tgbot.keyboards.all_replykeyboard import Reply_board
from tgbot.misc.states import Admin_all_message
from tgbot.misc.states import Admin_add_st
from tgbot.misc.states import Admin_send_message_st


async def admin_com1(message: Message):
    await message.answer(f"Привет, Admin {message.from_user.first_name}, доступные команды ниже⌨",
                         reply_markup=Reply_board().admin_keyboards())


async def add_admin1(message: Message):
    await message.answer("Enter user id")
    await Admin_add_st.st1.set()


async def add_admin2(message: Message, state: FSMContext):
    user_id = message.text
    await message.answer(f"Admin added with id {user_id}")
    await state.finish()


async def admin_send_all1(message: Message):
    print("admin_send1")
    await message.answer("Оберіть", reply_markup=Inner_board.inline_for_sto("Для всіх", "Для клієнтів"))
    await Admin_all_message.st1.set()


async def admin_notice1(message: Message):
    await message.answer("Напишите id пользователя")
    await Admin_send_message_st.st1.set()


async def admin_notice2(message: Message, state: FSMContext):
    await state.update_data(id=message.text)
    await message.answer("Хорошо, теперь напишите сообщение для отправки")
    await Admin_send_message_st.st2.set()


async def admin_notice3(message: Message, state: FSMContext):
    await message.answer("Сообщение отправлено")
    await state.finish()


async def admin_send_all2(call: CallbackQuery, state: FSMContext):
    await state.update_data(whom=call.data)
    await call.message.answer("Хорошо, в каком виде будет рассылка",
                              reply_markup=Inner_board.inline_for_sto("Только текст", "Фото и текст"))
    await Admin_all_message.st2.set()


async def admin_send_all3(call: CallbackQuery, state: FSMContext):
    await state.update_data(how=call.data)
    await call.bot.edit_message_text("Введи текст для рассылки", call.message.chat.id, call.message.message_id)
    await Admin_all_message.st3.set()


async def admin_send_all4(message: Message, state: FSMContext):
    await state.update_data(mes_text=message.text)
    data = await state.get_data()
    if data.get("how") == "Фото и текст":
        await message.answer("Пришлите фото для рассылки")
        await Admin_all_message.st4.set()
    else:
        await Admin_all_message.st4.set()
        await admin_send_all5(message, state)


async def admin_send_all5(message: Message, state: FSMContext):
    data = await state.get_data()
    if data.get("how") == "Фото и текст":
        await message.bot.send_photo(message.chat.id, message.photo[0].file_id, caption=data.get("mes_text"))
        await message.answer("Будет отправлено сообщение више в таком виде, вы уверены?",
                             reply_markup=Inner_board.inline_for_sto("Да, отправить", "Нет, отменить"))
    else:
        await message.answer(data.get("mes_text"))
        await message.answer("Будет отправлено сообщение више в таком виде, вы уверены?",
                             reply_markup=Inner_board.inline_for_sto("Да, отправить", "Нет, отменить"))
    await Admin_all_message.st5.set()


async def admin_send_all6(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Рассылка успешна, количество отправлений ???💠")
    await state.finish()


def register_admin_com(dp: Dispatcher):
    dp.register_message_handler(admin_com1, commands="admins_help", state="*", is_admin=True)
    dp.register_message_handler(admin_notice1, text="Повідомлення клієнту", state="*", is_admin=True)
    dp.register_message_handler(admin_notice2, state=Admin_send_message_st.st1)
    dp.register_message_handler(admin_notice3, state=Admin_send_message_st.st2)
    dp.register_message_handler(add_admin1, text="Додати адміністратора", state="*", is_admin=True)
    dp.register_message_handler(add_admin2, state=Admin_add_st.st1)
    dp.register_message_handler(admin_send_all1, text="Створити оголошення усім", state="*", is_admin=True)
    dp.register_callback_query_handler(admin_send_all2, text=["Для клієнтів", "Для всіх"], state=Admin_all_message.st1)
    dp.register_callback_query_handler(admin_send_all3, text=["Только текст", "Фото и текст"],
                                       state=Admin_all_message.st2)
    dp.register_message_handler(admin_send_all4, state=Admin_all_message.st3)
    dp.register_message_handler(admin_send_all5, state=Admin_all_message.st4, content_types=ContentTypes.ANY)
    dp.register_callback_query_handler(admin_send_all6, text=["Да, отправить", "Нет, отменить"],
                                       state=Admin_all_message.st5)

