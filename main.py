import telebot
from config import TOKEN_TG_BOT
from bot.handlers import register_handlers

TOKEN = TOKEN_TG_BOT
bot = telebot.TeleBot(TOKEN)

# Регистрация обработчиков
register_handlers(bot)

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)