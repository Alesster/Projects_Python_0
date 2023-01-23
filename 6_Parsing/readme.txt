Parsing news in website
https://www.youtube.com/watch?v=9onddoBnkRc&list=PLqGS6O1-DZLoAADhgzzkvc8ifKsKG4G-T&index=8
https://www.youtube.com/watch?v=cfcn1-EzSbc&list=PLqGS6O1-DZLoAADhgzzkvc8ifKsKG4G-T&index=9

pip install requests bs4 lxml

We use website:
https://www.securitylab.ru/news/

Convert Unix time to Human-readable time:
https://www.epochconverter.com/

For using Telegram:
pip install aiogram

Create new file tg_bot.py
import datetime
import json
from aiogram import Bot, Dispatcher, executor, types
from config import token

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

types.ParseMode.HTML - for activation of HTML tegs.

from aiogram.utils.markdown import hbold, hunderline, hcode, hlink => methods of markdown instead of HTML

For Buttons activation:
@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["All news", "Last 5 news", "Fresh news"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

from aiogram.dispatcher.filters import Text => for exact coinsidience handlers with buttons
Use filters in handlers:
@dp.message_handler(Text(equals="All news"))

Use module asyncio to check news peridically:
import asyncio




