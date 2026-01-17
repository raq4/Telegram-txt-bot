import os
import telebot
import io

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: m.text and not m.text.startswith('/'))
def work(m):
    f = io.BytesIO(m.text.encode())
    f.name = 'text.txt'
    bot.send_document(m.chat.id, f)

print("Bot started!")
bot.infinity_polling()
