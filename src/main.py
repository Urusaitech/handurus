import asyncio
import aiojobs
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from datetime import datetime

from handlers import commands
from src.handlers import subscription
from src.handlers import notifications
from src.settings.config import config

bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())


async def scheduler():
    from src.handlers.notifications import background_collect_updates, background_send_updates
    schedule = aiojobs.Scheduler()

    await schedule.spawn(background_collect_updates())
    await schedule.spawn(background_send_updates())


async def main():
    logging.basicConfig(level=logging.INFO)
    dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    dp.include_routers(commands.router, subscription.router, notifications.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await scheduler()
    await dp.start_polling(bot, mylist=[1, 2, 3])


if __name__ == "__main__":
    print('launching bot')
    asyncio.run(main())
