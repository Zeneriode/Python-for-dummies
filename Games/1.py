# Угадай число
# 1 игрок загадывает число, второй отгадывает
# 1 из игроков - компьютер

# 1 часть игры - загадывает число человек, компьютер отгадывает
from random import randint as rnd

numbers = list(range(1, 11))

for i in range(len(numbers)):
    number = numbers[rnd(0, len(numbers) - 1)]
    print("Ты загадал число ", number, "?", sep="")
    answer = int(input())
    if answer == 0:
        numbers.remove(number)
    else:
        print("Ура")
        break
