import pygame.key
from pygame import *  # импортируем библиотеку pygame для создания игр
from time import sleep


init()  # просто создаём пустое поле
# display.set_caption("Game")  # задаём название для поля
screen = display.set_mode([800, 600])  # задаём размеры для поля

red = (255, 0, 0)  # я для примера создал 3 переменные - 3 разных цвета по шкале RGB (Google в помощь, что это:) )
green = (0, 255, 0)
blue = (0, 0, 255)

img = image.load("../Module 3/snake_head.png")
img_rect = img.get_rect()

x = 100
y = 100

r = Rect(x, y, 50, 10)  # создадим объект - прямоугольник с определенными координатами и размерами
draw.rect(screen, red, r)  # нарисуем этот прямоугольник на нашем поле
screen.blit(img, (5, 5))


# async def move():
#     global x, y
#     if key.key_code("d"):
#         x = x + 1
#         y = y + 1
#     sleep(3)


play = True  # просто переменная, которая будет помогать фиксироваться цикл
while play:  # создаём бесконечный цикл
    for e in event.get():  # проверяем, что мы делаем на нашем поле
        if e.type == QUIT:  # если мы нажали на крестик, то
            play = False    # просто закрываем наше окно
    draw.rect(screen, red, r)  # нарисуем этот прямоугольник на нашем поле
    screen.blit(img, (5, 5))
    r = Rect(x, y, 50, 50)  # создадим объект - прямоугольник с определенными координатами и размерами
    # move()
    # print(x, y)
    # draw.rect(screen, "blue", Rect(0, 0, 800, 600))
    display.update()  # обновляем поле - если появится что-то новое, то оно рисуется или изменится

# sleep(3)  # если мы оставляем окно постоянно открытым, то хотя бы просто удержим его на 3 секунды
