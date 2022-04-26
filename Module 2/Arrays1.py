"""
Занятие 6 - изучение массивов
Массивы - переменные, которые сохраняют несколько значений вместе.
Самый простой и популярный тип массивов - списки.
Списки похожи на то, что мы используем в жизни, например, список покупок для магазина.
В Python вместо покупок (названий продуктов) мы сохраняем некоторые значения, которые потом сможем использовать.
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # список - сохранены значения от 1 до 10

# В список можно сохранять любые типы в любом порядке
a = [True, 1, 1531, "Привет", a, "Еще переменная", 5.2, 8754324256465, -65]

# Используя цикл, можно создать список любой длины и любых значений
a = list(i for i in range(1, 11))  # то же самое, что и на 9 строке
# команда list() создает список

# Чтобы выбрать определенный элемент из списка, используем индексы - адрес элемента в списке
print(a[0])  # Выпишется 1, в списках индексы начинаются с 0 и идут по порядку - a[1], a[2] ... a[9]

# Списки можно срезать - отделять от них части
print(a[:9])  # Чтобы "отрезать" часть с конца списка - пишем ':' и число справа, выпишется [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Чтобы "отрезать" с начала списка - пишем аналогично, но число уже слева от ':'
print(a[1:])  # Выпишется [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Срезать можно одновременно и слева, и справа
print(a[2:8])  # [3, 4, 5, 6, 7, 8]

# Также можно брать часть элементов с каким-то интервалом - для этого пишем два раза ':', а далее справа шаг
print(a[::2])  # Выпишется [1, 3, 5, 7, 9] - используются индексы 0, 2, 4, 6, 8, то есть от начала до конца с шагом 2

# с помощью таких срезов легко разворачивать список
print(a[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Все работает так же, как пишется в range() - можно ничего не писать, а можно использовать все 3 числа
print(a[1:8:2])  # [2, 4, 6, 8]

# строки работают так же, как и списки - можно использовать все, что есть у списков
print("Привет это надо стереть"[:6])  # Выпишется только "Привет" - срез строки

# Списки могут выполнять несколько новых команд
# Тут есть список команд, которые можно совершать со списками
a.append(5)  # добавляем в конец списка значение 5
a.pop(0)  # удаляем первый элемент списка
a.remove(5)  # удаляем первую попавшуюся значение 5 (если их не будет в списке, будет ошибка)
a.count(5)  # считает кол-во элементов со значением 5
a.index(5)  # выведет номер элемента со значением 5
a.sort()  # сортирует список
a.reverse()  # аналог a[::-1]
a.clear()  # удаляет все элементы из списка
print(len(a))  # выводит кол-во элементов в списке
print(sum(a))  # выводит сумму всех элементов в списке
print(max(a))  # или min(a) - выводит максимальное/минимальное значение из списка
# некоторые команды работают также со словарями, кортежами и множествами, это можно протестировать

# у массивов в Python работает reference - если изменить копию списка, то оригинальный список тоже изменится
b = a  # делаем копию списка
b[0] += 1  # увеличиваем первый элемент на 1
print(a, b)  # первый элемент увеличился у обоих списков на 1, хотя увеличивали только у одного
# См. что такое reference (индусы на Youtube в помощь)

# из списков можно создавать матрицы - списки в списке
matrix = [[0] * 10] * 10  # матрица 10 на 10, заполненная нулями
multiply_table = list(list(i * j for i in range(1, 11)) for j in range(1, 11))  # таблица умножения - матрица