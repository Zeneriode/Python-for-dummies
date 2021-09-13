import datetime


def find_unique():
    """Вывести количество уникальных значений в списке"""
    objects = list(map(int, input().split()))
    ans = 0
    t = []
    for obj in objects:
        if obj not in t:
            t.append(obj)
            ans += 1
    print(ans)


def find_even():
    """Выписать четные числа от 2 до n"""
    n = int(input())
    for i in range(2, n+1, 2):
        print(i)
    # Или print(i if i % 2 == 0)


def closest_mod_5(x):
    """Найти ближайшее число к Х, делящееся на 5 и больше самого Х"""
    return x if x % 5 == 0 else x + (5 - x % 5)


def c(n, k):
    """Найти количество различных подмножеств во множестве, тут рекурсия"""
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return c(n - 1, k) + c(n - 1, k - 1)


def foo():
    """Возвращаем ошибку (см. следующую функцию)"""
    return 1 / 0


def try_catch():
    """Ловим ошибки"""
    try:
        foo()
    except ZeroDivisionError:
        return "Делить на 0 нельзя"


def find_day():
    """Дано дата и кол-во дней -> найти дату через кол-во этих дней"""
    y, m, d = map(int, input().split())
    plus_day = int(input())

    curr_date = datetime.date(y, m, d)
    next_date = curr_date + datetime.timedelta(plus_day)
    clear_next_day = str(next_date.year) + " " + str(next_date.month) + " " + str(next_date.day)
    return clear_next_day


def replace_a_to_b():
    """Надо посчитать минимальное кол-во замен a на b в c, или вывести impossible если таких операций больше 1000"""
    s = input()
    a = input()
    b = input()
    answer = 0
    while a in s:
        prev = s
        s = s.replace(a, b)
        if (prev in s) or (a in b) or answer > 1000:
            answer = "Impossible"
            break
        answer += 1
    return answer


def t_in_s():
    """Вывести кол-во раз вхождений t в c"""
    s = input()
    t = input()
    cnt, pos = 0, 0
    while True:
        idx = s[pos:].find(t)
        if idx != -1:
            cnt += 1
            pos += idx + 1
        else:
            break
    return cnt


def copy_files():
    """Выписать в другой файл буквы в кол-ве, написанном после буквы"""
    with open("input.txt", "r") as f:
        inputs = f.readline()
    inputs += " "
    with open("output.txt", "w") as f:
        outputs = ""
        i = 0
        try:
            while True:
                if inputs[i] == str(inputs[i]):
                    x = inputs[i]
                    i += 1
                    number = 0
                    try:
                        while True:
                            number += number * 10 + int(inputs[i])
                            i += 1
                    except ValueError:
                        for j in range(number):
                            outputs += x
        except IndexError:
            f.write(outputs)


def fibonacci(n):
    """Выписать номер числа из последовательности Фибоначчи"""
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
