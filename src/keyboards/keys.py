from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_hi = KeyboardButton('Hi! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)


inline_btn_1 = InlineKeyboardButton('Take part', callback_data='callJoin')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)

inline_btn_about = InlineKeyboardButton('About bot', callback_data='callAbout')
inline_btn_help = InlineKeyboardButton('Help', callback_data='callHelp')
inline_kb_full.add(inline_btn_about, inline_btn_help)
inline_kb_full.insert(InlineKeyboardButton("Leaderboard", callback_data='callLeader'))

inline_cancel = InlineKeyboardButton('cancel', callback_data='callCancel')
cancel_mu = InlineKeyboardMarkup(row_width=2).add(inline_cancel)
