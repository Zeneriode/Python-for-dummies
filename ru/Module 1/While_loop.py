# 4 занятие - цикл while и использование модулей

# для создания случайных данных нужно использовать дополнительные модули Python - random
from random import randint as rnd  # из этой библиотеки мы возьмем одну функцию - randint

n = rnd(0, 1351)  # берем случайное число от 0 до 1351

a = 0  # Просто переменные
b = 7

# Иногда надо повторять одно и то же в программе. Для этого мы используем цикл
# while - повторение некоторого кода до невыполнения условия перед ':'
while a != b:  # цикл, который будет выполняться, пока a не равно b
    print(a)
    a += 1

while True:  # бесконечный цикл - условие всегда выдает True
    print(b)
    if n == 7:
        break  # если надо, мы можем остановить цикл, используя спец. команду

while 1 == 1:  # еще бесконечный цикл
    if n == 0:
        continue  # с помощью этого цикл продолжится с новой итерации, а код ниже не будет выполнен
    print(1)