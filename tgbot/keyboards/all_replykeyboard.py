from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dataclasses import dataclass


@dataclass
class Reply_board:
    request_location: bool = False
    request_contact: bool = False
    one_time_keyboard: bool = False
    row_width: int = 2
    input_field_placeholder: str = "Select button"

    def replay_keyboard(self, *args):
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=self.one_time_keyboard,
                                 row_width=self.row_width, input_field_placeholder=self.input_field_placeholder)
        for i in range(len(args)):
            kb.add(KeyboardButton(text=args[i], request_contact=self.request_contact,
                                  request_location=self.request_location))
        return kb

    def replay_serv_city(self, *args):
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=self.one_time_keyboard,
                                 row_width=self.row_width, input_field_placeholder=self.input_field_placeholder)
        kb.add(KeyboardButton(text=args[0]), KeyboardButton(args[1]), KeyboardButton(args[2]), KeyboardButton(args[3]))

        return kb

    def replay_authorization(self, *args):
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=self.one_time_keyboard,
                                 row_width=self.row_width, input_field_placeholder=self.input_field_placeholder)

    def replay_start1(self, *args):
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=self.one_time_keyboard,
                                 row_width=self.row_width, input_field_placeholder=self.input_field_placeholder)
        return kb.add(KeyboardButton(text="/info"), KeyboardButton(text="Особистий кабінет"))

    def replay_start2(self):
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=self.one_time_keyboard,
                                 row_width=self.row_width, input_field_placeholder=self.input_field_placeholder)
        return kb.add(KeyboardButton(text="Відправити контакт", request_contact=True),
                      KeyboardButton(text="Повернутись назад"))

    def replay_start3(self):
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=self.one_time_keyboard,
                                 row_width=self.row_width, input_field_placeholder=self.input_field_placeholder)
        return kb.add(KeyboardButton(text="/help"))

        # kb.add(KeyboardButton)
