import pygame
import sys

speed = [0, 0]

screen = pygame.display.set_mode((800, 680))
screen.fill([255, 255, 255])

ball = pygame.draw.rect(screen, 'blue', (20, 20, 80, 80))

pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ball.move(speed)
    if ballrect.left < 0 or ballrect.right > 680:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > 800:
        speed[1] = -speed[1]

    screen.blit(screen, ball)
    pygame.display.flip()
