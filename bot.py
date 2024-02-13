import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.admin_handlers.message_all_user import register_message_all_user
from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.admin_handlers.admin import register_admin
from tgbot.filters.creator import CreatorFilter
from tgbot.handlers.all_status import register_all_status
from tgbot.handlers.echo import register_echo
from tgbot.handlers.info import register_info
# from tgbot.handlers.my_words import register_my_word
from tgbot.handlers.service import register_serv_cto
from tgbot.handlers.help import register_help
from tgbot.handlers.id import register_id
from tgbot.handlers.start import register_user
from tgbot.handlers.support import register_support
# from tgbot.handlers.test_for_creator import register_test_command
from tgbot.middlewares.environment import EnvironmentMiddleware

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(CreatorFilter)


def register_all_handlers(dp):
    register_admin(dp)
    register_message_all_user(dp)
    # register_test_command(dp)

    register_user(dp)
    # register_my_word(dp)
    register_info(dp)
    register_all_status(dp)
    register_id(dp)
    register_help(dp)
    register_support(dp)
    register_serv_cto(dp)

    register_echo(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
