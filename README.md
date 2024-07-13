# Telegram Bot & Bitrix 24 API
<img src="https://privet-rostov.ru/templates/privet-rostov4/images/goog5.png">

## Описание

Этот проект представляет собой Telegram-бота, который принимает заказы на услуги и отправляет их в Bitrix24. 
Бот последовательно запрашивает у пользователя информацию о желаемой услуге, имени и телефоне, после чего отправляет эти данные в Bitrix24 с помощью вебхука.

## Конфигурация

В файле `config.py` в корневой директории проекта и добавьте в него следующую информацию.
```python
TOKEN_TG_BOT = 'your-telegram-bot-token'
API_BITRIX24_HOOK = 'your-bitrix24-webhook-url/crm.lead.add'
```
## Структура проекта
```
telegram_bot_project/
├── config.py
├── main.py
├── requirements.txt
├── README.md
└── bot/
    ├── __init__.py
    ├── handlers.py
    └── bitrix.py
```

## ⚖️ Лицензия

````
Этот проект лицензирован под лицензией MIT.