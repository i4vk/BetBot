import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
import json

config = json.loads(open("config.json", 'r').read())

token = config['token']
print(token)

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola bro, que pasa!")

def addLeague(update, context):
    keyboard = [[KeyboardButton("Crear", callback_data='1'),
                KeyboardButton("Eliminar", callback_data='2')]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    update.message.reply_text('Elige una opción:', reply_markup=reply_markup)
    

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

league_handler = CommandHandler('add_league', addLeague)
dispatcher.add_handler(league_handler)

updater.start_polling()