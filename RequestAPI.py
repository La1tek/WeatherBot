import requests
import Functions
import Arguments
from telebot import types
import pymorphy2

def GetResult(bot, message, city):
  res = requests.get(Functions.make_url(city))
  if (res.json()["cod"] == 200) and city != "None":
    # data = json.load(res.text)
    temp = res.json()["main"]["temp"]
    temp_fells = res.json()["main"]["feels_like"]
    humidity = res.json()["main"]["humidity"]
    city = res.json()["name"]
    if city[-1] != 'о':
      city = pymorphy2.MorphAnalyzer().parse(city)[0].inflect({'loct'}).word.title()
    city_id = res.json()["id"]
    weather = res.json()["weather"][0]["main"]
    if weather in Arguments.Text.name_ico:
      ico = Arguments.Text.emoji_list[weather]
    else:
      ico = ""
    weather_desc = res.json()["weather"][0]["description"]
    text = f'''
Сейчас в {city} {weather_desc} {ico}
Температура составляет {temp}°С
Ощущается как {temp_fells}°С
Влажность {humidity}%
    '''
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(types.InlineKeyboardButton("Открыть в браузере 🌎", url=f"https://openweathermap.org/city/{city_id}"))
    bot.reply_to(message, text, reply_markup= markup)
  else:
    bot.send_message(message.chat.id, "Город не найден")

def CorrectCity(city):
  res = requests.get(Functions.make_url(city))
  if (res.json()["cod"] == 200):
    return True
  else:
    return False

def GetCity(city):
  res = requests.get(Functions.make_url(city))
  city = res.json()["name"]
  return city