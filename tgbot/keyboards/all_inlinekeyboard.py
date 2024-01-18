from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dataclasses import dataclass


@dataclass
class Inner_board:
    """creates inline button"""
    row_width: int = 2
    link: str = None

    # @staticmethod
    # def keyboard_coffee():
    #     mark = InlineKeyboardMarkup(row_width=2)
    #     return mark.add(InlineKeyboardButton(text="touch me", callback_data="touch"),
    #                     # "https://www.youtube.com/channel/UCcm00p5w8nPQ2INFv8waXJg"
    #                     InlineKeyboardButton(text="My Youtube", callback_data="link"))
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
    def start_inline():
        mark = InlineKeyboardMarkup(row_width=1)
        return mark.add(InlineKeyboardButton(text="help", callback_data="help"))
