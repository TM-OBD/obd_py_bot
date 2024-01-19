from aiogram.dispatcher.filters.state import StatesGroup, State


class Admin_all_message_state(StatesGroup):
    s1 = State()
    s2 = State()


class Add_word(StatesGroup):
    firstandlast = State()
