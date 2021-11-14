from pygame import *
# from time import sleep


init()
display.set_caption("Game")
screen = display.set_mode([600, 800])

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

r = Rect(100, 100, 50, 50)
draw.rect(screen, red, r)

play = True
while play:
    for x in event.get():
        if x.type == QUIT:
            play = False
    display.update()

# sleep(3)
