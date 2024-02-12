from aiogram import Dispatcher
from aiogram.types import Message, ContentType

from tgbot.keyboards.all_replykeyboard import Reply_board
from tgbot.models.Main_requests_to_server import MainRequests


async def user_start1(message: Message):
    await message.answer("Привіт, я бот для користувачів OBD. Якщо хочеш дізнатися детальніше, натисни кнопку /info,"
                         " але якщо хочеш зареєструватися, натискай відповідну кнопку нижче.🔽",
                         reply_markup=Reply_board().replay_start1())


async def user_start2(message: Message):
    if MainRequests.is_authorized():
        if MainRequests.is_client():
            await message.answer("You are client")
        else:
            await message.answer("Нажаль, ви не є нашим клієнтом.")
    # await message.answer("", reply_markup=Reply_board().replay_start2())
    else:
        await message.answer("Для реєстрації необхідно поділитися контактом. 🙇",
                             reply_markup=Reply_board().replay_start2())


async def user_start3(message: Message):
    user_id = message.from_user.id
    contact_id = message.contact.user_id
    if user_id == contact_id:
        if not MainRequests.is_authorized():
            MainRequests.authorization()
            if MainRequests.is_client():
                await message.answer("Ви успішно зареєстровані!",
                                     reply_markup=Reply_board(one_time_keyboard=True).replay_start3())
            else:
                await message.answer("Нажаль, ви не є нашим клієнтом.",
                                     reply_markup=Reply_board(one_time_keyboard=True).replay_keyboard(
                                         "Повернутись назад"))


async def user_back(message: Message):
    await user_start1(message)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start1, commands="start")
    dp.register_message_handler(user_start2, text="Особистий кабінет")
    dp.register_message_handler(user_start3, content_types=ContentType.CONTACT)
    dp.register_message_handler(user_back, text="Повернутись назад")
