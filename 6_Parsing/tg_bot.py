import asyncio
import datetime
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from config import token, user_id
from main import check_news_update, get_first_news

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["All news", "Last 5 news", "Fresh news"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    
    await message.answer("List of news", reply_markup=keyboard)
    
#@dp.message_handler(commands="all_news")
@dp.message_handler(Text(equals="All news"))
async def get_all_news(message: types.Message):
    news_dict = get_first_news()
    
    # with open("news_dict.json") as file:
    #     news_dict = json.load(file)
        
#    print(news_dict)

    for k, v in sorted(news_dict.items()) :
        # news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n" \
        #     f"<u>{v['article_title']}</u>\n" \
        #     f"<code>{v['article_desc']}</code>\n" \
        #     f"{v['article_url']}"
        # news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
        #     f"{hunderline(v['article_title'])}\n" \
        #     f"{hcode(v['article_desc'])}\n" \
        #     f"{hlink(v['article_title'], v['article_url'])}"
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
            f"{hlink(v['article_title'], v['article_url'])}"
            
        await message.answer(news)
        
#@dp.message_handler(commands="last_five")
@dp.message_handler(Text(equals="Last 5 news"))
async def get_last_five(message: types.Message):
    news_dict = get_first_news()
    
    # with open("news_dict.json") as file:
    #     news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
            f"{hlink(v['article_title'], v['article_url'])}"   
            
        await message.answer(news)   
        
#@dp.message_handler(commands="fresh_news")
@dp.message_handler(Text(equals="Fresh news"))
async def get_fresh_news(message: types.Message):  
    fresh_news = check_news_update()
    
    if len(fresh_news) >=1:
        for k, v in sorted(fresh_news.items()):
            news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                f"{hlink(v['article_title'], v['article_url'])}"   
                
            await message.answer(news) 
    else:
        await message.answer("There are no news yet ... ")
        
async def news_every_minute():
    while True:
        fresh_news = check_news_update()
        
        if len(fresh_news) >=1:
            for k, v in sorted(fresh_news.items()):
                news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                    f"{hlink(v['article_title'], v['article_url'])}"   
                    
                # get your id @userinfobot
                await bot.send_message(user_id, news, disable_notification = True)
                #await bot.send_message(message.from_user.id, news, disable_notification = True)
                #await message.reply(news)
        else:
            await bot.send_message(user_id, "There are no news yet ... ", disable_notification = True)
            #await message.reply("There are no news yet ... ")
    
        await asyncio.sleep(20)
        
if __name__=='__main__':
    get_first_news()
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp)