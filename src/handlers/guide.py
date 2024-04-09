import asyncio
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove

from src.settings.config import config

router = Router()
photo_id = config.busted_chats_pic.get_secret_value()


@router.message(F.text.lower() == "how to use")
async def answer_faq(message: Message):
    await message.answer(
        "Welcome to short guide on how to use this bot! \n\nIf you are tired of chats looking like this:",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer_photo(
        photo_id
    )
    await message.answer(
        " - then you are in the right place"
    )
    await asyncio.sleep(3)
    await message.answer(
        ("First of all, add your channels you are willing to optimize, one by one. \n"
         "To do so, enter /start command and choose <b>'Settings'</b> - <b>'Add Subscription'</b>\n(1/3)"),
        parse_mode="html"
    )
    await asyncio.sleep(2)
    await message.answer(
        ("After you've done with that, think about what are the key points of your channels that you don't want to "
         "miss.\n"
         "The bot uses <b>keywords</b> conception to filter news, if there is something containing your keyword - "
         "it will appear in your optimized news feed\n(2/3)"),
        parse_mode="html"
    )
    await asyncio.sleep(3)
    await message.answer(
        ("To set them up, go to <b>'Settings'</b> - <b>'Edit keyword'</b>\n"
         "The bot will show examples of how to send things for everything to work fine.\n"
         "Please note that the bot is in early development stage, some issues might occur, and there are a lot "
         "functionality to come. \nIf you feel like contacting the dev, there is a button in the start menu\n(3/3)"),
        parse_mode="html"
    )
