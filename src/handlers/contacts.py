from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()


@router.message(F.text.lower() == "contacts")
async def answer_faq(message: Message):
    await message.answer(
        "dev: @urusaitech",
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="html",
    )
