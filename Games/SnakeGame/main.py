from pygame import init, time, event
from snake_settings import *

fps = time.Clock()

init()  # запускаем файл, окно

land = Land(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)  # Задний фон для игры

start_x = randint(BLOCK_SIZE * 4, SCREEN_WIDTH - BLOCK_SIZE * 5)
start_y = randint(0, SCREEN_HEIGHT)
snake = Snake("green", start_x - start_x % BLOCK_SIZE, start_y - start_y % BLOCK_SIZE, 4)

play = True
while play:
    snake.change_direction()
    snake.move()

    play = snake.check_collisions()

    land.draw()
    snake.draw()

    # рисуем границы между блоками в окне
    for i in range(BLOCK_SIZE, SCREEN_WIDTH, BLOCK_SIZE):
        draw.line(screen, "black", [i, 0], [i, SCREEN_HEIGHT])
    for i in range(BLOCK_SIZE, SCREEN_HEIGHT, BLOCK_SIZE):
        draw.line(screen, "black", [0, i], [SCREEN_WIDTH, i])

    for e in event.get():  # проверим, что мы хотим выйти из игры
        if key.get_pressed()[pygame.K_ESCAPE] or e.type == pygame.QUIT:
            play = False

    display.update()
    fps.tick(8)
