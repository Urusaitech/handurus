from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Yes")
    kb.button(text="No")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def get_start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="List subs")
    kb.button(text="Settings")
    kb.button(text="FAQ")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def get_settings_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Add subscription")
    kb.button(text="Notifications frequency")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
