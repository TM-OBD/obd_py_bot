import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.config import Config


class CreatorFilter(BoundFilter):
    key = 'is_creator'

    def __init__(self, is_creator: typing.Optional[bool] = None):
        self.is_creator = is_creator

    async def check(self, obj):
        if self.is_creator is None:
            return False
        config: Config = obj.bot.get('config')
        return (obj.from_user.id == config.tg_bot.creator) == self.is_creator

