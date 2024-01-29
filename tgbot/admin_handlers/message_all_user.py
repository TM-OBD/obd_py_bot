from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from tgbot.keyboards.all_inlinekeyboard import Inner_board
from tgbot.misc.states import Admin_all_message_state

"""Функции для передачи сообщения всем users"""


async def func_message_all_user(message: Message):
    await message.answer("Введите сообщение:")
    await Admin_all_message_state.s1.set()


async def func_message_all_user2(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer=answer)
    await message.answer("Вы уверены?", reply_markup=Inner_board.all_message_YorN())
    await Admin_all_message_state.s2.set()


async def func_message_all_user3(call: CallbackQuery, state: FSMContext):
    if call.data == "all_no":
        await state.finish()
    else:
        n = 0
        data = await state.get_data()
        admin_text = data.get("answer")
        try:
            for i in range(n):
                await call.bot.send_message(chat_id=i, text=admin_text)
            await call.bot.send_message(call.from_user.id, "Сообщения были отосланы успешно")
        except Exception as e:
            await call.bot.send_message(call.from_user.id, "Что-то пошло не так, ошибка:")
            await call.bot.send_message(call.from_user.id, text=f"{e}")
        finally:
            await state.finish()


def register_message_all_user(dp: Dispatcher):
    dp.register_message_handler(func_message_all_user, commands="all_users_message", state=None, is_admin=True)
    dp.register_message_handler(func_message_all_user2, state=Admin_all_message_state.s1)
    dp.register_callback_query_handler(func_message_all_user3, text=["all_yes", "all_no"], state=Admin_all_message_state.s2)
