
# SMTPHelperBot

SMTPHelperBot — это Telegram-бот, который позволяет пользователям отправлять письма прямо из Telegram. Бот собирает email пользователя и текст сообщения, а затем отправляет письмо через SMTP сервер Яндекса.

## Функции
- Запрашивает у пользователя email.
- Проверяет корректность формата email.
- Просит ввести текст сообщения.
- Отправляет письмо через SMTP сервер Яндекса.

## Как использовать

1. **Начало работы с ботом**  
   Найдите в Telegram бота `@SMTPHelperBot` и нажмите **Старт**.

2. **Введите ваш email**  
   Бот попросит вас ввести ваш email. Убедитесь, что введён правильный email (например, `user@example.com`).

3. **Введите текст сообщения**  
   После того как email принят, бот попросит вас ввести текст сообщения.

4. **Сообщение отправлено**  
   После того как сообщение введено, бот отправит письмо на указанный email.

## Требования

- **Аккаунт в Telegram** для общения с ботом.
- **Аккаунт Яндекса** для использования их SMTP сервера для отправки писем.
  
Убедитесь, что ваш email Яндекса и пароль настроены правильно в переменных окружения бота.

## Установка

1. Клонируйте этот репозиторий:
   ```bash
   git clone https://github.com/MaGmYmS/SMTP-Telegram-bot
   ```

2. Установите необходимые библиотеки Python:
   ```bash
   pip install aiogram
   ```

3. Настройте переменные окружения для токена Telegram-бота и учётных данных SMTP Яндекса:
   - `TELEGRAM_BOT_TOKEN`: Ваш токен Telegram-бота.
   - `SMTP_USER`: Ваш email Яндекса (например, `your_email@yandex.ru`).
   - `SMTP_PASSWORD`: Ваш пароль или пароль для приложения Яндекса.

4. Запустите бота:
   ```bash
   python bot.py
   ```
