import aiohttp
from aiogram.types import Message

from src.settings.config import config


class Subscriptions:
    def __init__(self):
        self.parser_host = config.parser_host.get_secret_value()

    async def process_new_subscription(self, message: Message):
        print('we got url ', message.text)
        data = {'user': message.from_user.id, 'url': message.text}

        async with aiohttp.ClientSession() as session:
            response = await session.post(url=f'{self.parser_host}/api/v1/channel',
                                          json=data,
                                          headers={"Content-Type": "application/json"})
            print(await response.json())

    @staticmethod
    async def get_subscriptions(user_id: int):
        pass
