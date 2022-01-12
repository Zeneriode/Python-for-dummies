from random import randint as rnd


def human_guess_number() -> None:
    """Запускает игру, где человек угадывает число от 1 до 10, которое загадал компьютер"""
    number = rnd(1, 10)
    while True:
        answer = int(input())
        if answer == number:
            print("Ай молодец!")
            break
        else:
            print("Попробуй ещё раз.")


def computer_guess_number() -> None:
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


human_guess_number()
