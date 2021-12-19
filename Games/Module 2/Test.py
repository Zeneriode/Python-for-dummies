# Task 1: создать список чисел от 1 до 10
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 1 способ

a = []  # 2 способ
for i in range(1, 11):
    a.append(i)

a = list(i for i in range(1, 11))  # 3 способ


# Task 2: выписать только четные числа из списка, список случайный
a = list(map(int, input().split()))

# 1 способ
for x in a:
    if x % 2 == 0:
        print(x)

# 2 способ
for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i])


# Task 3: вывести факториал числа
def factorial(b):
    if b == 1:
        return 1
    return b * factorial(b)


factorial(int(input()))
