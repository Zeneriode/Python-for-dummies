"""Разработка бота для Discord: основные пункты"""

import recommend_logging  # Рекомендуемое использование библиотеки logging, чтобы ошибки и дебагинг были читаемы
import discord  # У этой библиотеки также есть документации, весь код в открытом доступе + есть сервер с разработками

# Для работы со скрытыми данными, чтобы никто кроме вас не получил доступ к боту
from dotenv import load_dotenv, find_dotenv
from os import getenv

# Создаем клиента - внутрення оболочка бота в Python коде
client = discord.Client()

# Парсим наш .env file, чтобы программа могла находить там ключи
load_dotenv(find_dotenv())


# В первую очередь следует залогиниться в бота. Для этого надо использовать команду on_ready
@client.event  # Этот декоратор использует верхнюю функцию для работы с ботом, в большинстве случае используется он
async def on_ready():
    """Выводит сообщение в случае удачно попытки входа в аккаунт бота"""
    print(f"Connected. Bot is {client}")


@client.event
async def on_message(message: discord.Message):
    """Отвечает на сообщения, отправленные боту.
        :param message сообщение, которое было отправлено в чате"""

    # Прежде всего нужно проверить, что сообщения пришло от другого пользователя, а не от бота самому себе
    if message.author == client.user:
        return

    # Пример отправки - на сообщение "Hello" мы ответим "Hello back"
    if message.content.startswith("$Hello"):  # $ в начале помогает определить, что сообщение адресовано именно боту
        await message.channel.send("Hello back")


if __name__ == "__main__":  # Запускаем нашего бота с помощью команды run()
    client.run(getenv("token"))
