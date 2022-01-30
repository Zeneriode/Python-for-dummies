from pygame import *

# Константы
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
BLOCK_SIZE = 25
DELAY = 60

init()  # запускаем файл, окно

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # окно


class Land(Rect):
    """Задний фон игры"""
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.background = "#FFFFFF"

    def draw(self):
        """Рисует задний фон в виде прямоугольника на все окно"""
        global screen  # где мы будем рисовать наш фон
        draw.rect(screen, self.background, [self.left, self.top, self.width, self.height])


land = Land(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)  # Задний фон для игры

play = True
while play:
    for e in event.get():
        if e.type == QUIT:
            play = False

    land.draw()
    display.update()
