https://home.openweathermap.org/
alesster
pogoda_09

My API Key
Create key => name: myAPI_key => Generate

pip install requests

in web-site we look server for getting weather:
Built-in API request by city name 
https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

Use pprint to rganize json
from pprint import pprint

in this case: pprint(data)

We have the data in unit SI. To convert it to normal unit, put at the end of url: &units=metric

Время в секундах с 01.01.1970
Для перевода в нормальное время используется:
import datetime
datetime.datetime.fromtimestamp(time in seconds)

For using in Telegram
pip install aiogram

main.py - for testing
main_weather_tg_bot.py - for creating telegram chat bot
