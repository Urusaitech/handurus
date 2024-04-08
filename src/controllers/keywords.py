import aiohttp
from aiogram.types import Message

from src.settings.config import config


class Keywords:
    def __init__(self):
        self.parser_host = config.parser_host.get_secret_value()

    async def add_keywords_for_user(self, message: Message):
        print('adding keywords ', message.text)
        async with aiohttp.ClientSession() as session:
            keywords = message.text.split(',')
            keywords = {
                "user_tg": message.from_user.id,
                "keywords": keywords
            }
            print(keywords)
            response = await session.post(url=f'{self.parser_host}/api/v1/keywords/{message.from_user.id}',
                                          json=keywords,
                                          headers={"Content-Type": "application/json"})
            result = await response.json()
            print(result)