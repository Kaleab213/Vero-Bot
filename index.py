from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

conversation_options = ["Greeting", "Informational", "Fun fact", "Joke", "Weather", "News", "Translation"]

updater = Updater(token='your-token-here', use_context=True)

def start(update, context):
    keyboard = [[option] for option in conversation_options]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am Vero. Kal's chatbot. Please choose a conversation option:", reply_markup=reply_markup)

def handle_greeting(update, context):
    keyboard = [[option] for option in conversation_options]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm not great at social interactions, but I'll try my best. Hello! How are you doing?", reply_markup=reply_markup)

def handle_informational(update, context):
    keyboard = [[option] for option in conversation_options]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Here's some information for you...", reply_markup=reply_markup)

def handle_fun_fact(update, context):
    keyboard = [[option] for option in conversation_options]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Did you know that? Hippopotomonstrosesquippedaliophobia is the fear of long words.", reply_markup=reply_markup)

def handle_joke(update, context):
    keyboard = [[option] for option in conversation_options]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Why do programmers wear glasses? Because they can't C#", reply_markup=reply_markup)

def handle_weather(update, context):
    keyboard = [[option] for option in conversation_options]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="The weather is currently sunny and 25 degrees Celsius.", reply_markup=reply_markup)

def handle_news(update, context):
    keyboard = [[option] for option in conversation_options]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="In the news today...", reply_markup=reply_markup)

def handle_translation(update, context):
    keyboard = [[option] for option in conversation_options]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Here's your translation...", reply_markup=reply_markup)

def unknown(update, context):
    keyboard = [[option] for option in conversation_options]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.", reply_markup=reply_markup)

# Add handlers for each conversation option
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Greeting$'), handle_greeting))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Informational$'), handle_informational))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Fun fact$'), handle_fun_fact))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Joke$'), handle_joke))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Weather$'), handle_weather))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^News$'), handle_news))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Translation$'), handle_translation))
# updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))

if __name__ == '__main__':
    updater.start_polling()
    while True:
        pass


# code below is written with an effort to add the bot to personal account but it failed.

# updater.start_polling()
# updater.idle()

# from telethon import TelegramClient, events, sync

# api_id = 'your_api_id'
# api_hash = 'your_api_hash'
# phone_number = '+251901711106'

# client = TelegramClient('user_session', api_id, api_hash)

# client.connect()
# if not client.is_user_authorized():
#     client.send_code_request(phone_number)
#     client.sign_in(phone_number, input('Enter the code: '))

# @client.on(events.NewMessage(incoming=True))
# async def handle_new_message(event):
#     if event.is_private:  # only respond to private messages
#         await event.respond('I received your message')

# client.run_until_disconnected()
