# Test 1 - написать как можно больше разных типов переменных
# 4, 5.2, Hello, True; 5.2, 4, H, 0
a = int(input())
b = float(input())
c = str(input())
d = bool(input())

# Test 2 - сравнить 2 числа всеми возможными способами
# 2 и 5 - false, true, false (true), false (true); 3 и 3 - true, false, false (false), true (true)
print(a == b)
print(a != b)
print(a > b)  # <
print(a >= b)  # <=

# Test 3 - проверить, является ли год високосным
# 2020 - високосный, 2021 - невисокосный, 2000 - високосный, 1500 - невисокосный
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Високосный")
else:
    print("Невисокосный")

# Test 4 - написать факториал числа
# 0 - 1, 1 - 1, 2 - 2, 3 - 6, 4 - 24, 5 - 120
n = int(input())
fac = 1
while n > 0:
    fac *= n
    n -= 1
print(fac)
