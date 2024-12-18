import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy! How are you doing?")

@bot.message_handler(func = lambda message : True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.infinity_polling()