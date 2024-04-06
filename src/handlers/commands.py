from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.formatting import Bold, Text

from src.keyboards.main_kbs import get_start_kb, get_settings_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Use navigation buttons",
        reply_markup=get_start_kb()
    )


@router.message(F.text.lower() == "list subs")
async def answer_subs(message: Message):
    await message.answer(
        "No subscriptions yet",
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


