from telebot import TeleBot
from bot.bitrix import send_to_bitrix24

# Словарь для хранения данных от пользователя
user_data = {}

def register_handlers(bot: TeleBot):
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