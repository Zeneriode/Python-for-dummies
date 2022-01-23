# считывать имя и возраст, вывести "Привет, {имя}. Тебе {возраст} лет!"
name = input()
age = int(input())
print("Привет, ", name, ". Тебе ", age, "лет!", sep="")

# Считывать координаты 2 клеток на шахматной доске, проверить, может ли король за 1 ход попасть из одной клетки в другую
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if -1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1:
    print("Может")
else:
    print("Не может")

# Считывать координаты 2 клеток и написать, за сколько ходов ладья, слон и ферзь дойдут из одной клетки в другую.
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(1 if x1 == x2 or y1 == y2 else 2)  # ладья
print(1 if abs(x1 - x2) == abs(y1 - y2) else 2)  # офицер
print(1 if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2) else 2)  # ферзь

# Дан год, вывести, високосный он или нет
year = int(input())
print("Високосный" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "Невисокосный")
