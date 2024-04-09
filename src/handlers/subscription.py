from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from src.controllers.keywords import Keywords
from src.controllers.subscriptions import Subscriptions
from src.settings.config import config

router = Router()

url_regex = r"^(?:https?:\/\/)?t.me\/[a-zA-Z0-9_]{5,32}$"


class Subscribe(StatesGroup):
    receiving_url = State()
    receiving_keywords = State()


@router.message(F.text.lower() == "add subscription")
async def add_subscription(message: Message, state: FSMContext):
    await message.answer(
        "send url, example: https://t.me/telegram",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Subscribe.receiving_url)


@router.message(F.text.lower() == "notifications frequency")
async def edit_keywords(message: Message, state: FSMContext):
    rate = int(config.updates_rate.get_secret_value()) // 60
    await message.answer(
        f"Section in development, current feeds update rate: {rate} min",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text.lower() == "edit keywords")
async def edit_keywords(message: Message, state: FSMContext):
    await message.answer(
        ("Send keywords, example: <b>blackout,climate change,promot</b>\n\n"
         "✏️Tips for better accuracy:\n"
         "- don't put spaces between keywords\n"
         "- use words without endings if the ending changes frequently\n\n"
         "Note that this action will override your current keywords.\n"
         "/start to cancel"),
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="html"
    )
    await state.set_state(Subscribe.receiving_keywords)


@router.message(Subscribe.receiving_url, F.text.regexp(url_regex))
async def url_correct(message: Message, state: FSMContext):
    await state.update_data(chosen_food=message.text.lower())
    await message.answer(
        text=f"Channel {message.text.replace("https://t.me/", "@")} will appear in your feed soon",
    )
    await Subscriptions().process_new_subscription(message)
    await state.clear()


@router.message(Subscribe.receiving_url)
async def url_incorrect(message: Message):
    await message.answer(
        text="Channel not found, \n/start - main menu",
    )


@router.message(Subscribe.receiving_keywords)
async def url_incorrect(message: Message):
    data = "Added keywords:\n"
    for num, word in enumerate(message.text.split(','), start=1):
        data += f"{num}. {word}\n"
    await message.answer(
        text=data,
        reply_markup=ReplyKeyboardRemove()
    )
    await Keywords().add_keywords_for_user(message=message)
