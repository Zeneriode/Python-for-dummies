# Угадай число
# 1 игрок загадывает число, второй отгадывает
# 1 из игроков - компьютер

# 1 часть игры - загадывает число человек, компьютер отгадывает

from random import randint as rnd
# python      ->          c      ->        assembly language      ->          machine code
#        interpretation       compiler     MIPS X86             assembler
# c#, c++, c - абсолютно разные


def guess_number() -> None:
    number = rnd(1, 10)
    while True:
        answer = int(input())
        if answer == number:
            print("Ай молодец!")
            break
        else:
            print("Попробуй ещё раз.")


guess_number()


def find_number() -> None:
    numbers = list(range(1, 11))  # список чисел, которые компьютер может угадывать

    for i in range(len(numbers)):
        number = numbers[rnd(0, len(numbers) - 1)]  # берет случайное число из списка
        print("Ты загадал число ", number, "?", sep="")
        answer = int(input())
        if answer == 0:
            numbers.remove(number)
        else:
            print("Ура")
            break
