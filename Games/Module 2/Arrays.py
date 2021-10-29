aa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # список
aa = list(i for i in range(1, 11))  # такой же список

print(aa[:9])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(aa[1:])  # [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(aa[2:8])  # [3, 4, 5, 6, 7, 8]
print(aa[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(aa[1:8:2])  # [2, 4, 6, 8]

# СТРОКИ - ЭТО СПИСКИ ДЛЯ КОМПЬЮТЕРА, С НИМИ МОЖНО РАБОТАТЬ ТАКЖЕ

aaa = {1: 0, 2: 'a', 5: 'g', 'a': 4}  # словарь
print(aaa['a'])

a = {1, 2, 3, 4, 5}  # по английски кортеж
a = tuple(i for i in range(1, 6))
# кортеж не изменяется, поэтому нельзя писать a4[1] = ...

aaaa = (1, 2, 3, 4, 5, 6)  # множество
aaaa = set(i for i in range(1, 7))
# множество хранит только уникальные значения, элементы не повторяются
# список может быть [1, 2, 3, 3, 3], а такое же множество (1, 2, 3)

bb = aa  # делаем копию списка
bb[0] += 1  # увеличиваем первывй элемент на 1
print(aa, bb)  # первый элемент увеличился у обоих списоков на 1, хотя увеличивали только у одного
# см. что такое поинтер (индусы на Ютубе в помощь)
