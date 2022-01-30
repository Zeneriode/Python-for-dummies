from pygame import display, draw, Rect
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
        self.background = "#FFFFFF"

    def draw(self):
        """Рисует задний фон в виде прямоугольника на все окно"""
        global screen  # где мы будем рисовать наш фон
        draw.rect(screen, self.background, (self.left, self.top, self.width, self.height))


class Snake:
    global screen
    """Змейка"""
    def __init__(self, color, start_x, start_y, body_parts):
        self.size = BLOCK_SIZE
        self.color = color
        self.direction = 'r'
        self.body_parts = body_parts
        self.x = list((start_x - i) for i in range(0, body_parts * BLOCK_SIZE, BLOCK_SIZE))
        self.y = list(start_y for i in range(0, body_parts * BLOCK_SIZE, BLOCK_SIZE))

    def draw(self):
        for body in range(self.body_parts):
            draw.rect(screen, self.color, (self.x[body], self.y[body], self.size, self.size))

    def move(self):
        """Двигаем змейку на один блок"""
        pass

    def check_collisions(self):
        """Проверяем, что змейка не врезалась в себя и не вышла за границы"""
        pass

    def grow(self):
        """Змейка растет от поедания еды"""
        pass

    def change_direction(self):
        """Меняем направление головы змейки"""
        pass


if __name__ == "__main__":
    x = randint(BLOCK_SIZE * 4, SCREEN_WIDTH - BLOCK_SIZE * 5)
    y = randint(0, SCREEN_HEIGHT)
    snake = Snake("green", x - x % BLOCK_SIZE, y - y % BLOCK_SIZE, 4)
    print(*snake.x, *snake.y)
    snake.move()
    snake.change_direction()
