import os
import telebot
import io

TOKEN = os.environ["8225246869:AAH10vhRzkHJu7N6FVmur0aO8ZVy-41yzM"]
bot = telebot.TeleBot(TOKEN)

print("🚀 Бот запускается...")

@bot.message_handler(func=lambda m: m.text and not m.text.startswith('/'))
def make_txt(message):
    try:
        # Создаём файл
        file = io.BytesIO(message.text.encode('utf-8'))
        file.name = 'text.txt'
        
        # Отправляем
        bot.send_document(
            message.chat.id, 
            file,
            caption="✅ Файл готов!"
        )
        
        print(f"📤 Файл отправлен для {message.from_user.id}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

# Игнорируем команды
@bot.message_handler(func=lambda m: m.text and m.text.startswith('/'))
def ignore(message):
    pass

print("✅ Бот работает! Ожидаю сообщения...")
bot.infinity_polling()
