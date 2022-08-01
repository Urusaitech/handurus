from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import BOT_TOKEN
import keys as kb

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


##

class JoinContest(StatesGroup):
    waiting_for_bet_slip = State()


@dp.message_handler(commands=['start'])
async def process_command_start(message: types.Message):
    await message.answer('Handurus bot is launched!',
                         reply_markup=kb.inline_kb_full)


help_message = text(
    'Commands:\n',
    '/start - launch',
    '/soon - see upcoming futures',
    '/leaderboard - top users',
    '/about - learn about the bot',
    sep='\n'
)
about_message = text(
    'About in development!'
)
join_message = text(
    'Send the number'
)
leader_message = text(
    ...
)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    print('help needed')  # for debugging
    await message.answer(help_message)


@dp.callback_query_handler(text_contains='call')
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data

    if code == 'callHelp':
        await bot.send_message(callback_query.from_user.id, help_message)

    elif code == 'callAbout':
        await bot.send_message(callback_query.from_user.id, about_message)

    elif code == 'callJoin':
        await bot.send_message(callback_query.from_user.id, join_message)
        await JoinContest.waiting_for_bet_slip.set()

    elif code == 'callLeader':
        await bot.send_message(callback_query.from_user.id, leader_message)

    else:
        ...


##


@dp.message_handler(commands=['soon'])
async def process_command_1(message: types.Message):
    await message.answer('You will see it here soon',
                         reply_markup=kb.cancel_mu)
    # needed cancel button


if __name__ == '__main__':
    executor.start_polling(dp)
