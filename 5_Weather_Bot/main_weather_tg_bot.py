import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hi! Write please name of the city and I will give you Weather condition")
    
@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Fog": "Fog \U0001F32B",
        "Mist": "Mist \U0001F32B"
    }
    
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        
        city = data["name"]
        weather_type = data["weather"][0]["description"]
        clouds = data["clouds"]["all"]
        
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look to the street!"
        
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        wind_speed_kt = wind_speed*1.944012
        wind_dir = data["wind"]["deg"]
        visibility = data["visibility"]
        sunrise_timestamp=datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp=datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"])-datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        
        await message.reply(f" *** {datetime.datetime.now().strftime('%d-%m-%y %H:%M')} *** \n"
            f"Weather in: {city}\n{wd}\nWeather: {weather_type}\nClouds: {clouds} %\nTemperature: {temperature} C°\n"
            f"Humidity: {humidity} %\nPressure: {pressure} HPa\nWind speed: {wind_speed} m/s = {wind_speed_kt:.2f} kt\n"            
            f"Wind direction: {wind_dir} deg\nVisibility: {visibility} m\n"
            f"Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nLength of the day: {length_of_day}\n\n"
            f"Best wishes!\nAbbracci forti!\nAbrazos fuertes!\nВсего наилучшего!")
        
        
    except:
        await message.reply("\U00002620 Check city name \U00002620")    
    
if __name__=='__main__':
    executor.start_polling(dp)