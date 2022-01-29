from pygame import *

init()

screen = display.set_mode((800, 600))

play = True
while play:
    for e in event.get():
        print(e, e.type)
        if e.type == QUIT:
            play = False

    display.update()
