from aiogram.dispatcher.filters.state import StatesGroup, State


class Admin_all_message_state(StatesGroup):
    s1 = State()
    s2 = State()


class Add_word(StatesGroup):
    firstandlast = State()


class State_cto(StatesGroup):
    st1 = State()
    st2 = State()
    st3 = State()
    st4 = State()
    st5 = State()
    st6 = State()
    st7 = State()


class End_state(StatesGroup):
    end_state = State()


class Test_state(StatesGroup):
    st1 = State()
    st2 = State()
    # st3 = State()
