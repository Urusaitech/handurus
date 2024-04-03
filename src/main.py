import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from datetime import datetime

from aiogram.fsm.storage.memory import MemoryStorage
from handlers import commands
from src.handlers import subscription

from src.settings.config import config


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    dp.include_routers(commands.router, subscription.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, mylist=[1, 2, 3])


if __name__ == "__main__":
    asyncio.run(main())
