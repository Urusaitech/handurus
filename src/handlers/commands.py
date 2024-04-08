import aiohttp
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.formatting import Bold, Text

from src.keyboards.main_kbs import get_start_kb, get_settings_kb
from src.settings.config import config

router = Router()
parser_host = config.parser_host.get_secret_value()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Use navigation buttons",
        reply_markup=get_start_kb()
    )


@router.message(F.text.lower() == "list subs")
async def answer_subs(message: Message):
    async with aiohttp.ClientSession() as session:
        print("sending request")
        await message.answer(
                "Loading..",
                reply_markup=ReplyKeyboardRemove()
            )
        response = await session.get(url=f"{parser_host}/api/v1/channels/{message.from_user.id}",
                                     headers={"Content-Type": "application/json"})
        result = await response.json()
        print(result)
        if not result["subs"]:
            await message.answer(
                "No subscriptions yet",
                reply_markup=ReplyKeyboardRemove()
            )
        else:
            data = "Your subscriptions:\n"
            for i in result["subs"]:
                data += f"{i.replace("https://t.me/s/", "@")}\n"
            await message.answer(
                data,
                reply_markup=ReplyKeyboardRemove()
            )


@router.message(F.text.lower() == "list keywords")
async def answer_keywords(message: Message):
    async with aiohttp.ClientSession() as session:
        print("sending kw request")
        await message.answer(
                "Loading..",
                reply_markup=ReplyKeyboardRemove()
            )
        response = await session.get(url=f"{parser_host}/api/v1/keywords/{message.from_user.id}",
                                     headers={"Content-Type": "application/json"})
        result = await response.json()
        print(result)
        if not result["keywords"]:
            await message.answer(
                "No keywords added yet",
                reply_markup=ReplyKeyboardRemove()
            )
        else:
            data = "Your keywords:\n"
            for num, word in enumerate(result["keywords"], start=1):
                data += f"{num}. {word}\n"
            await message.answer(
                data,
                reply_markup=ReplyKeyboardRemove()
            )


@router.message(F.text.lower() == "settings")
async def answer_settings(message: Message):
    await message.answer(
        "choose an option",
        reply_markup=get_settings_kb()
    )


@router.message(F.text.lower() == "faq")
async def answer_faq(message: Message):
    await message.answer(
        "In development",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command("info"))
async def cmd_info(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        **Text(
            "your TG id: ", Bold(message.from_user.id)
        ).as_kwargs()
    )
