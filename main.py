from telebot import types
from Arguments import Text, bot, activity
from Functions import Buttons
import Functions
import requests
import DB
import RequestAPI

# ---------------- Команда /start ---------------- #

@bot.message_handler(commands = [Text.start_command]) # Команда /start
def start(message):
  DB.AddID(message.from_user.id, message.from_user.first_name, message.chat.username)
  DB.Log(message.from_user.id, "/start")
  bot.send_message(message.chat.id, Text.welcome,  reply_markup = Buttons.start())

# ---------------- Хендлер коллбеков ---------------- #

@bot.callback_query_handler(func = lambda call:True)
def response(function_call):
  if function_call.message:
    DB.Log(function_call.message.chat.id, "InlineButton" + function_call.data)
    if function_call.data == "start": # Коллбек с кнопки при /start
      bot.edit_message_text(chat_id= function_call.message.chat.id, message_id=function_call.message.id, text= Text.start_quest, reply_markup = Buttons.skip())
      bot.answer_callback_query(function_call.id)
      activity[function_call.message.chat.id] = "Waiting city"
    if function_call.data == "skip": # Коллбек с кнопки пропуска выбора города
      activity[function_call.message.chat.id] = "Working"
      bot.edit_message_text(chat_id= function_call.message.chat.id, message_id=function_call.message.id, text= Text.start_skip, reply_markup = None)
      bot.send_message(function_call.message.chat.id, Text.main, reply_markup=Buttons.buttons_keyboard(function_call.message.chat.id))
    if function_call.data == "correct": # Город выбран корректно
      bot.edit_message_text(chat_id= function_call.message.chat.id, message_id=function_call.message.id, text= Text.settings_city_confirm, reply_markup = None)
      bot.send_message(function_call.message.chat.id, "Введи любой город и я расскажу о погоде в нем", reply_markup=Buttons.buttons_keyboard(function_call.message.chat.id))
      activity[function_call.message.chat.id] = "Working"
    if function_call.data == "not_correct": # Город выбран некорректно
      bot.edit_message_text(chat_id= function_call.message.chat.id, message_id=function_call.message.id, text= "Введи свой город", reply_markup = None)

# ---------------- Хендлер сообщений ---------------- #

@bot.message_handler(content_types=["text"])
def handle_text(message):
    DB.Log(message.from_user.id, message.text)
    if message.chat.id not in activity.keys():
      activity[message.chat.id] = "Working"
    if activity[message.chat.id] != "Waiting city":
      if (message.text.strip() == Text.button_weather):
        RequestAPI.GetResult(bot, message, DB.View_city(message.from_user.id))
      elif (message.text.strip() == Text.button_city):
        activity[message.chat.id] = "Waiting city"
        bot.send_message(message.chat.id, "Введи свой город")
      else:
        city = message.text.strip().lower()
        # DB.City(message.from_user.id, city)
        RequestAPI.GetResult(bot, message, city)
    else:
      if message.text.strip() == "Не сейчас":
        bot.send_message(chat_id= message.chat.id, text= Text.start_skip, reply_markup = None)
        activity[message.chat.id] = "Working"
      else:
        city = message.text.strip()
        if (RequestAPI.CorrectCity(city)):
          DB.City(message.from_user.id, city)
          ans_city = RequestAPI.GetCity(city)
          bot.send_message(message.chat.id, f"Твой город - {ans_city}. Верно?", reply_markup=Buttons.select_city())
        else:
          bot.send_message(message.chat.id, Text.settings_city_error)


bot.polling(none_stop = True, interval = 0)