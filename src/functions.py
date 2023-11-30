from telebot import types

from arguments import Text
import arguments as arguments
import db

def change_city():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton(Text.welcome_res)
    keyboard.add(item)
    return keyboard

def make_url(city):
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={arguments.api_key}&units=metric&lang=ru"
  return url


class Buttons(object):
  
  def start():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text = 'Приступим', callback_data='start'))
    return markup

  def skip():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Не сейчас, напишу потом", callback_data='skip'))
    return markup  

  def select_city():
    markup = types.InlineKeyboardMarkup(row_width = 2)
    not_corr = types.InlineKeyboardButton(text=Text.condition[0],callback_data='not_correct')
    corr = types.InlineKeyboardButton(text=Text.condition[1],callback_data='correct')
    markup.add(not_corr, corr)
    return markup
  
  def buttons_keyboard(id):
      markup = types.ReplyKeyboardMarkup(row_width = 3, resize_keyboard=True)
      print(id)
      print(db.View_city(id))

      if db.View_city(id) != "None":
        markup.add(types.KeyboardButton(text = Text.button_weather))
      markup.add(types.KeyboardButton(text = Text.button_city))
      return markup    

