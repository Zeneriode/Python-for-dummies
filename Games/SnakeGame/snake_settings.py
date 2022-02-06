import pygame
from typing import Union
from pygame import display, draw, Rect, key, Color
from random import randint

# константы
BLOCK_SIZE = 35
SCREEN_WIDTH = BLOCK_SIZE * 25
SCREEN_HEIGHT = BLOCK_SIZE * 20
DELAY = 60

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # окно


class Land(Rect):
    """Задний фон игры"""
    def __init__(self, *args):
        super().__init__(*args)
        self.background = "#FFFFFF"  # задний фон окна

    def draw(self):
        """Рисует задний фон в виде прямоугольника на все окно"""
        global screen  # где мы будем рисовать наш фон
        draw.rect(screen, self.background, (self.left, self.top, self.width, self.height))


class Snake:
    global screen
    """Змейка"""
    def __init__(self, color: Union[str, Color], start_x: int, start_y: int, body_parts: int):
        self.size = BLOCK_SIZE  # размеры змейки
        self.color = color  # цвет змейки
        self.direction = 'r'  # направление движения головы змеи
        self.body_parts = body_parts  # кол-во блоков (включая голову)
        self.x = list((start_x - i) for i in range(0, body_parts * BLOCK_SIZE, BLOCK_SIZE))  # координаты по x всех блоков
        self.y = list(start_y for i in range(0, body_parts * BLOCK_SIZE, BLOCK_SIZE))  # координаты по y всех блоков

    def draw(self):
        """Рисует все блоки для змейки"""
        global screen
        for body in range(self.body_parts):
            draw.rect(screen, self.color, (self.x[body], self.y[body], self.size, self.size))

    def move(self):
        """Двигаем змейку на один блок"""

        # двигаем всю часть змеи, кроме головы
        for i in range(len(self.x) - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # двигаем голову в соответствии с направлением движения
        match self.direction:
            case 'r': self.x[0] += BLOCK_SIZE
            case 'l': self.x[0] -= BLOCK_SIZE
            case 'u': self.y[0] -= BLOCK_SIZE
            case 'd': self.y[0] += BLOCK_SIZE

    def check_collisions(self):
        """Проверяем, что змейка не врезалась в себя и не вышла за границы"""
        pass

    def grow(self):
        """Змейка растет от поедания еды"""
        pass

    def change_direction(self):
        """Меняем направление головы змейки"""
        if key.get_pressed()[pygame.K_w] and self.direction != 'd':  # вверх
            self.direction = 'u'
        if key.get_pressed()[pygame.K_a] and self.direction != 'r':  # влево
            self.direction = 'l'
        if key.get_pressed()[pygame.K_s] and self.direction != 'u':  # вниз
            self.direction = 'd'
        if key.get_pressed()[pygame.K_d] and self.direction != 'l':  # вправо
            self.direction = 'r'


if __name__ == "__main__":
    snake = Snake("white", 1, 1, 4)
    while True:
        # for k in key.get_pressed():
        #     if k:
        # print(snake.direction)
        snake.change_direction()
