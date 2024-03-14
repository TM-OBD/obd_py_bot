from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dataclasses import dataclass


@dataclass
class Inner_board:
    """creates inline buttons"""
    row_width: int = 2
    link: str = None

    # @staticmethod
    # def keyboard_coffee():
    #     mark = InlineKeyboardMarkup(row_width=2)
    #     return mark.add(InlineKeyboardButton(text="touch me", callback_data="touch"),
    #                     # "https://www.youtube.com/channel/UCcm00p5w8nPQ2INFv8waXJg"
    #                     InlineKeyboardButton(text="My", callback_data="link"))
    #
    # @staticmethod
    # def keyboard_show_word():
    #     mark = InlineKeyboardMarkup(row_width=2)
    #     return mark.add(InlineKeyboardButton(text="Yes", callback_data="Yes"),
    #                     InlineKeyboardButton(text="Show all", callback_data="show_all"))
    #
    # def start_inlineboar(self, *args):
    #     inline_markup = InlineKeyboardMarkup(row_width=self.row_width)
    #     for i in range(len(args)):
    #         inline_markup.add(
    #             InlineKeyboardButton(text=args[i], callback_data=args[i], login_url=self.link))
    #     return inline_markup

    @staticmethod
    def inline_for_sto(*args):
        mark = InlineKeyboardMarkup(row_width=2)
        for i in range(len(args)):
            mark.add(InlineKeyboardButton(text=args[i], callback_data=args[i]))
        return mark

    @staticmethod
    def start_inline():
        mark = InlineKeyboardMarkup(row_width=2)
        return mark.add(InlineKeyboardButton(text="/info", callback_data="info"),
                        InlineKeyboardButton(text="/authorization", callback_data="authorization"))

    @staticmethod
    def all_message_YorN():
        mark = InlineKeyboardMarkup(row_width=2)
        return mark.add(InlineKeyboardButton(text="Yes", callback_data="all_yes"),
                        InlineKeyboardButton(text="No", callback_data="all_no"))

    @staticmethod
    def status_inlines():
        mark1 = InlineKeyboardMarkup(row_width=2)
        mark2 = InlineKeyboardMarkup(row_width=2)
        mark1.add(InlineKeyboardButton(text="Tiguan", callback_data="car1"),
                  InlineKeyboardButton(text="Bugatti Chiron Super Sport", callback_data="car2"))
        mark2.add(InlineKeyboardButton(text="back", callback_data="back"))
        return mark1, mark2

    @staticmethod
    def chat_with_manager1():
        mark = InlineKeyboardMarkup(row_width=2)
        mark.add(InlineKeyboardButton(text="Да", callback_data="chat_yes"),
                 InlineKeyboardButton(text="Нет", callback_data="chat_no"))
        return mark

    @staticmethod
    def chat_with_manager_exit():
        mark = InlineKeyboardMarkup()
        mark.add(InlineKeyboardButton(text="Выйти из чата", callback_data="exit_chat"))
