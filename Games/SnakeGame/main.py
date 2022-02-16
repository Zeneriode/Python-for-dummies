from pygame import init, time, event
from snake_settings import *

fps = time.Clock()

init()  # запускаем файл, окно

land = Land(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)  # Задний фон для игры


def start() -> None:
    """Создаем объекты и случайные координаты для змеи"""
    start_x = randint(BLOCK_SIZE * 4, SCREEN_WIDTH - BLOCK_SIZE * 5)
    start_y = randint(0, SCREEN_HEIGHT)
    start_snake = Snake("green", start_x - start_x % BLOCK_SIZE, start_y - start_y % BLOCK_SIZE, 4)
    start_food = Food()
    game(start_snake, start_food)


def game(game_snake: Snake, game_food: Food):
    """Рисуем игру, следим за происходящим в ней, обновляем экран"""
    global land, fps
    play = True
    while play:
        game_snake.change_direction()
        game_food = eat(game_snake, game_food)
        game_snake.move()

        play = game_snake.check_collisions()

        land.draw()
        game_food.draw()
        game_snake.draw()

        for e in event.get():  # проверим, что мы хотим выйти из игры
            if key.get_pressed()[pygame.K_ESCAPE] or e.type == pygame.QUIT:
                play = False

        display.update()
        fps.tick(8)


if __name__ == "__main__":
    start()
