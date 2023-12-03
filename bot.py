import telebot
import requests
from config import TOKEN_TG_BOT, API_BITRIX24_HOOK

TOKEN = TOKEN_TG_BOT
BITRIX_WEBHOOK_URL = API_BITRIX24_HOOK

bot = telebot.TeleBot(TOKEN)

# Словарь для хранения данных от пользователя
user_data = {}

# Обработчик команды start
@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, "Какую услугу вы хотите заказать?")
    bot.register_next_step_handler(msg, process_service_step)

def process_service_step(message):
    user_data['service'] = message.text
    msg = bot.send_message(message.chat.id, "Как вас зовут?")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    user_data['name'] = message.text
    msg = bot.send_message(message.chat.id, "Введите ваш телефон:")
    bot.register_next_step_handler(msg, process_phone_step)

def process_phone_step(message):
    user_data['phone'] = message.text
    # Отправка данных в Bitrix24
    send_to_bitrix24(user_data)
    bot.send_message(message.chat.id, "Спасибо, ваш заказ принят!")

def send_to_bitrix24(data):
    # Формирование данных для отправки
    payload = {
        'fields': {
            'TITLE': f"Заказ: {data['service']}",
            'NAME': data['name'],
            'PHONE': [{'VALUE': data['phone'], 'VALUE_TYPE': 'WORK'}],
            'COMMENTS': f"Заказанная услуга: {data['service']}"
        }
    }
    # Отправка данных в Bitrix24
    requests.post(BITRIX_WEBHOOK_URL, json=payload)

# Запуск бота
bot.polling(none_stop=True)
