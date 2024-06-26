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
    kb.button(text="My subs")
    kb.button(text="Settings")
    kb.button(text="My keywords")
    kb.button(text="Contacts")
    kb.button(text="How to use")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def get_settings_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Add subscription")
    kb.button(text="Notifications frequency")
    kb.button(text="Edit keywords")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
