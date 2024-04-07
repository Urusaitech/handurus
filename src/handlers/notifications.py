import asyncio
import aiohttp
from aiogram import Router

from src.main import bot
from src.settings.config import config

router = Router()


class Notifications:
    def __init__(self):
        self.parser_host = config.parser_host.get_secret_value()
        self.updates_timer = 60  # sec
        self.updates = None

    async def collect_notification_task(self):
        while True:
            async with aiohttp.ClientSession() as session:
                print('collecting updates')
                response = await session.get(url=f'{self.parser_host}/api/v1/updates',
                                             headers={"Content-Type": "application/json"})
                self.updates = await response.json()
                print(f'updates: {self.updates}')
            await asyncio.sleep(self.updates_timer)

    async def send_notification(self):
        while True:
            await asyncio.sleep(3)
            print('sending updates')
            if self.updates:
                await bot.send_message(528914637, "text")
                self.updates = None
            else:
                print('updates not found')
            await asyncio.sleep(self.updates_timer)


notif_inst = Notifications()


async def background_collect_updates():
    await asyncio.create_task(notif_inst.collect_notification_task())


async def background_send_updates():
    await asyncio.create_task(notif_inst.send_notification())
