import asyncio
import aiohttp
import aiojobs
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from datetime import datetime

from handlers import commands
from src.handlers import subscription, notifications, guide, contacts
from src.settings.config import config

bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())


async def scheduler():
    from src.handlers.notifications import background_collect_updates, background_send_updates
    schedule = aiojobs.Scheduler()

    await schedule.spawn(background_collect_updates())
    await schedule.spawn(background_send_updates())


async def start_updates():
    parser_host = config.parser_host.get_secret_value()
    async with aiohttp.ClientSession() as session:
        response = await session.patch(url=f'{parser_host}/api/v1/updates/start',
                                       headers={"Content-Type": "application/json"})
        response = await response.json()
        print(f'bd updates started: {response}')
    await asyncio.sleep(3)


async def main():
    logging.basicConfig(level=logging.INFO)
    dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    dp.include_routers(
        commands.router,
        subscription.router,
        notifications.router,
        guide.router,
        contacts.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await start_updates()
    await scheduler()
    await dp.start_polling(bot, mylist=[1, 2, 3])


if __name__ == "__main__":
    print('launching bot')
    asyncio.run(main())
