"""
Библиотека discord использует библиотеку logging, чтобы фиксировать ошибки при запуске программы. Поэтому, чтобы читать
их в нормальном виде, желательно использовать .log файл, который будет фиксировать и записывать историю всех ошибок.
"""
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
