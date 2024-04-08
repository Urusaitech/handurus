from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from src.controllers.keywords import Keywords
from src.controllers.subscriptions import Subscriptions

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


@router.message(F.text.lower() == "edit keywords")
async def edit_keywords(message: Message, state: FSMContext):
    await message.answer(
        "send keywords, example: word,word",
        reply_markup=ReplyKeyboardRemove()
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
    await message.answer(
        text=f"Added keywords: {message.text}",
        reply_markup=ReplyKeyboardRemove()
    )
    await Keywords().add_keywords_for_user(message=message)
