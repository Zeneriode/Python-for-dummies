x = int(input())
y = int(input())
tls = []


def find_squares(a, b):
    if min(a, b) == 1:
        for i in range(max(a, b)):
            tls.append(1)
        return 0
    elif min(a, b) == 0:
        return 0

    if a == b:
        tls.append(a)
        return 0
    elif a > b:
        tls.append(min(a, b))
        a -= b
    else:
        tls.append(min(a, b))
        b -= a
    find_squares(a, b)


find_squares(x, y)
print(*tls)
print(len(tls))
