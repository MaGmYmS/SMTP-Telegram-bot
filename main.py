import re
import smtplib
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types.message import ContentType
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Чтение переменных окружения
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.yandex.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 465))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

# Проверка токена
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не установлен!")

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Состояния пользователя
user_data = {}


@dp.message(Command(commands=["start"]))
async def start(message: Message):
    await message.answer("Привет! Введите ваш email:")
    user_data[message.chat.id] = {"step": "email"}


@dp.message(lambda message: user_data.get(message.chat.id, {}).get("step") == "email")
async def handle_email(message: Message):
    email = message.text
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        user_data[message.chat.id]["email"] = email
        user_data[message.chat.id]["step"] = "message"
        await message.answer("Email принят. Теперь введите текст сообщения:")
    else:
        await message.answer("Некорректный email. Попробуйте еще раз:")


@dp.message(lambda message: user_data.get(message.chat.id, {}).get("step") == "message")
async def handle_message(message: Message):
    email = user_data[message.chat.id]["email"]
    text = message.text

    try:
        # Формируем письмо с указанием кодировки UTF-8
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = email
        msg['Subject'] = "Сообщение от Telegram-бота"
        msg.attach(MIMEText(text, 'plain', 'utf-8'))

        # Отправка сообщения через SMTP
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)

        await message.reply(f"Сообщение успешно отправлено на {email}!")
    except Exception as e:
        await message.reply(f"Ошибка отправки: {e}")

    # Сброс данных пользователя
    user_data.pop(message.chat.id, None)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
