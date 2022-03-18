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
        self.x = list(
            (start_x - i) for i in range(0, body_parts * BLOCK_SIZE, BLOCK_SIZE))  # координаты по x всех блоков
        self.y = list(start_y for _ in range(0, body_parts * BLOCK_SIZE, BLOCK_SIZE))  # координаты по y всех блоков

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
            case 'r':
                self.x[0] += BLOCK_SIZE
            case 'l':
                self.x[0] -= BLOCK_SIZE
            case 'u':
                self.y[0] -= BLOCK_SIZE
            case 'd':
                self.y[0] += BLOCK_SIZE

    def check_collisions(self) -> bool:
        """Проверяем, что змейка не врезалась в себя и не вышла за границы"""

        # проверка пересечения змейки самой себя
        for i in range(1, len(self.x)):
            if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                return False  # если пересекаем сами себя, то останавливаем игру

        # пересекаем границу экрана
        if self.x[0] >= SCREEN_WIDTH:  # справа
            self.x[0] = 0
        if self.x[0] < 0:  # слева
            self.x[0] = SCREEN_WIDTH
        if self.y[0] >= SCREEN_HEIGHT:  # снизу
            self.y[0] = 0
        if self.y[0] < 0:  # сверху
            self.y[0] = SCREEN_HEIGHT

        return True  # если не пересекаем сами себя, то продолжаем игру

    def grow(self):
        """Змейка растет от поедания еды"""
        self.x.append(SCREEN_WIDTH * 2)  # добавляем новое тело змейки за пределы экрана
        self.y.append(SCREEN_HEIGHT * 2)
        self.body_parts += 1  # увеличиваем кол-во частей тел на 1

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


class Food:
    """Еда, которую будет поедать змейка"""

    def __init__(self):
        global BLOCK_SIZE
        self.x = randint(0, SCREEN_WIDTH) // BLOCK_SIZE * BLOCK_SIZE  # случайные координаты для еды
        self.y = randint(0, SCREEN_HEIGHT) // BLOCK_SIZE * BLOCK_SIZE
        self.size = BLOCK_SIZE  # размеры еды
        self.color = "red"  # цвет еды

    def draw(self):
        """Рисуем еду на экране"""
        global screen
        draw.rect(screen, self.color, Rect(self.x, self.y, self.size, self.size))


def eat(snake_: Snake, food_: Food) -> Food:
    """Едим еду, змейка растет, появляется новая еда"""
    if snake_.x[0] == food_.x and snake_.y[0] == food_.y:  # если координаты еды и змейки совпали
        snake_.grow()  # растим змейку
        food_ = Food()  # создаем новую еду (по факту просто координаты блока еды)

    return food_  # если еда съедена, возвращаем новый объект, если нет - вернем старые


if __name__ == "__main__":
    food = Food()
    snake = Snake("white", food.x, food.y, 4)
    while True:
        eat(snake, food)
