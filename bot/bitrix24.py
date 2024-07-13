import requests
from config import API_BITRIX24_HOOK

BITRIX_WEBHOOK_URL = API_BITRIX24_HOOK

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