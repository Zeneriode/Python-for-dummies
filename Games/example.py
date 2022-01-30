from pygame import event, init, QUIT
from snake_settings import *

init()  # запускаем файл, окно

land = Land(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)  # Задний фон для игры

start_x = randint(BLOCK_SIZE * 4, SCREEN_WIDTH - BLOCK_SIZE * 5)
start_y = randint(0, SCREEN_HEIGHT)
snake = Snake("green", start_x - start_x % BLOCK_SIZE, start_y - start_y % BLOCK_SIZE, 4)

play = True
while play:
    for e in event.get():
        if e.type == QUIT:
            play = False
    land.draw()
    snake.draw()

    # рисуем границы между блоками в окне
    for i in range(BLOCK_SIZE, SCREEN_WIDTH, BLOCK_SIZE):
        draw.line(screen, "black", [i, 0], [i, SCREEN_HEIGHT])
    for i in range(BLOCK_SIZE, SCREEN_HEIGHT, BLOCK_SIZE):
        draw.line(screen, "black", [0, i], [SCREEN_WIDTH, i])

    display.update()
