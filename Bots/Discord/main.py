"""Разработка бота для Discord: основные пункты"""

import recommend_logging  # Рекомендуемое использование библиотеки logging, чтобы ошибки и дебагинг были читаемы
import intents  # Работа с интентами
import discord  # У этой библиотеки также есть документации, весь код в открытом доступе + есть сервер с разработками

# Для работы со скрытыми данными, чтобы никто кроме вас не получил доступ к боту
from discord.ext import tasks
from dotenv import load_dotenv, find_dotenv
from os import getenv

# Парсим наш .env file, чтобы программа могла находить там ключи
load_dotenv(find_dotenv())


# Чтобы начать использовать бота, нужно создать ему класс, который будет создавать отдельные методы для бота
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.my_background_task.start()

    # В первую очередь следует залогиниться в бота. Для этого надо использовать команду on_ready
    async def on_ready(self):
        """Выводит сообщение в случае удачно попытки входа в аккаунт бота"""
        print(f"Connected. Bot is {self}")

    async def on_message(self, message: discord.Message):
        """Отвечает на сообщения, отправленные боту.
            :param message сообщение, которое было отправлено в чате"""
        # Прежде всего нужно проверить, что сообщения пришло от другого пользователя, а не от бота самому себе
        if message.author == self.user:
            return
        # Пример отправки - на сообщение "Hello" мы ответим "Hello back"
        if message.content.startswith("$Hello"):  # $ в начале помогает определить, что сообщение адресовано именно боту
            await message.channel.send("Hello back")

    # В чатах можно запускать постоянные действия, например: сообщение каждые 10 секунд
    @tasks.loop(seconds=60)  # эта функция будет запускаться каждые 10 секунд
    async def my_background_task(self):
        """Отправляет сообщение "New message" в один чат"""
        # Чтобы отправить сообщения в конкретный чат, надо отметить номер этого чата
        channel = self.get_channel(967883176225693769)
        await channel.send("New message")  # Это сообщение отправится в чат

    # Функции с постоянным действием в чатах нужно запускать при запуске приложения
    @my_background_task.before_loop  # надо использовать декоратор, который создан заранее в классе Client
    async def before_my_task(self):
        """Предотвращает запуск монотонных функций до входа в аккаунт ботом"""
        await self.wait_until_ready()  # Сначала ждем, пока бот войдет в аккаунт, потом запускаем постоянное действие

    # Чтобы выполнить какое-либо действие, когда появился новый пользователь, нужно использовать эту функцию
    @staticmethod
    async def on_member_join(member: discord.Member):
        """Приветствует нового пользователя, когда он появляется на сервере"""
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f"Welcome {member.mention} to {guild.name}!"
            await guild.system_channel.send(to_send)


if __name__ == "__main__":  # Запускаем нашего бота с помощью команды run()
    client = MyClient(intents=intents.intents)
    client.run(getenv("token"))
