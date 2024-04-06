import aiohttp
from aiogram.types import Message

from src.settings.config import config


class Subscriptions:
    def __init__(self):
        self.parser_host = config.parser_host.get_secret_value()

    async def process_new_subscription(self, message: Message):
        print('we got url ', message.text)
        data = {
            'url': message.text,
            'user': {
                'user_id': message.from_user.id,
                'nickname': message.from_user.username,
                'language': message.from_user.language_code,
            }
        }

        async with aiohttp.ClientSession() as session:
            print('sending request')
            response = await session.post(url=f'{self.parser_host}/api/v1/channel',
                                          json=data,
                                          headers={"Content-Type": "application/json"})
            result = await response.json()
            print(result)
            if not result['sub_created']:
                await message.reply("I checked, the sub was already in your list")

    @staticmethod
    async def get_subscriptions(user_id: int):
        pass
