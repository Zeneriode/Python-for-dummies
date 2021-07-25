import pygame

pygame.init()

# Настройка отображения счета
score = 0
textX = 10
textY = 10
font = pygame.font.Font('freesansbold.ttf', 16)

# Создаем окно
screen = pygame.display.set_mode((800, 600))


# Настройка заголовка и иконки
pygame.display.set_caption('Сквош')

# Бита
paddle = pygame.image.load('paddle.png')
posX = 348
posY = 580
changeX = 0

# Мячик
ball = pygame.image.load('ball.png')
ballX = 368
ballY = 556
changeBallX = 0
changeBallY = 0
play = 0


# Функции в игре
def player(x, y):
    screen.blit(paddle, (x, y))


def seeball(x, y):
    screen.blit(ball, (x, y))


def show_score(x, y):
    view_score = font.render('Счет: ' + str(score), True, (0, 0, 0))
    screen.blit(view_score, (x, y))


# Игровой цикл
run = True

while run:

    screen.fill((255, 255, 255))

    # Обрабатываем действие при нажатии на кнопку "Закрыть"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Подлючаем кнопки
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -1
                if play == 0:
                    changeBallX = -1

            elif event.key == pygame.K_RIGHT:
                changeX = 1
                if play == 0:
                    changeBallX = 1
            if event.key == pygame.K_SPACE:
                changeBallX = 1
                changeBallY = -1
                play = 1

        if event.type == pygame.KEYUP:
            changeX = 0
            if play == 0:
                changeBallX = 0

    # Вычсисляем координаты мяча
    ballX += changeBallX
    ballY += changeBallY
    # Устанавливаем границы экрана для мяча
    if play == 1:
        if ballX >= 776:
            changeBallX = -1
        elif ballX <= 0:
            changeBallX = 1
    else:
        if ballX == 776 or ballX == 0:
            changeBallX = 0

    if ballY == 0:
        changeBallY = 1

    # Изменяем направление движения мяча при столкновении с битой
    if play == 1:
        if ballY == 556:
            if posX - 22 < ballX < posX + 64:
                changeBallY = -1
                score += 1

    # Отображаем мяч
    seeball(ballX, ballY)

    # Отображаем счет
    show_score(textX, textY)

    # Вычисляем позицию биты
    posX += changeX

    # Устанавливаем границы для биты
    if posX <= 0:
        posX = 0
    elif posX >= 686:
        posX = 686

    # Отображаем биту
    player(posX, posY)

    # Обновляем экран
    pygame.display.update()
