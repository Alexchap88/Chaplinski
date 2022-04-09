import telebot
from telebot import types
#import api
#import database
#from decouple import config

token = 'esegsegsgsgsdbY'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_function(message):
    user_id = message.from_user.id
    print(message)

bot.polling(non_stop=True)