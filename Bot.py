import os
import telebot
import io

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: m.text and not m.text.startswith('/'))
def make_txt(message):
    file = io.BytesIO(message.text.encode('utf-8'))
    file.name = 'text.txt'
    bot.send_document(message.chat.id, file)

print("Бот работает!")
bot.infinity_polling()
