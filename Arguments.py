import telebot
from telebot import types
import sqlite3 as sql

# <<<<<<   #----------Bot_settings----------#   >>>>>> #

Token = "6713488438:AAGQKLgHiwDuH5cGXWucAgOH0M_2Fg6_xU0"
bot = telebot.TeleBot(Token)

api_key = "f90fa63a2bc73093977117767d2480d4"

activity = {}

#http://api.openweathermap.org/data/2.5/weather?q=Moscow&lang=ru&appid=f90fa63a2bc73093977117767d2480d4&units=metric

# <<<<<<   #----------SQL DATABASE----------#   >>>>>> #

class SQL():
  name_db = 'database.db'

class Text():

  #----------Welcome-------------#

  welcome = "Привет! Меня зовут Джимми, я универсальный метеобот, готов помочь тебе"

  start_quest = "Введи свой город, в дальнейшем буду присылать тебе погоду в нем :)"
  start_skip = "Хорошо, понял тебя! Можешь ввести свой город когда захочешь, для этого используй кнопку на клавиатуре"

  #----------Select city-------------#

  settings_city = "Введите название вашего города (населенного пункта)"
  settings_city_error = "Произошла ошибка :( Город не найден"
  settings_city_confirm = "Успешно ✓"

  #----------Main-------------#

  main = "Введи любой город и я расскажу о погоде в нем"

  button_weather = "Погода в моем городе ✨"
  button_city = "Ввести / изменить город"

  #----------EMOJI-------------#

  name_ico = ["Clear", "Clouds", "Rain", "Sunny", "Snow"]
  emoji_list = {
    "Clear":"☀️",
    "Clouds":"☁️",
    "Rain":"🌧",
    "Sunny":"⛈",
    "Snow":"🌨",
    "None":""
    }
  
  condition = ["❎","✅"]

  #----------Commands----------#

  start_command = "start"
