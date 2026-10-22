import math
def vvesti(imya):
    while True:
        try:
            return float(input("Введите " + imya + ": "))
        except ValueError:
            print("Это не число")
def poschitat(a, b, c):
    D = b * b - 4 * a * c
    print("Дискриминант =", D)
    if D < 0:
        ts = []
    elif D == 0:
        ts = [-b / (2 * a)]
    else:
        s = math.sqrt(D)
        ts = [(-b + s) / (2 * a), (-b - s) / (2 * a)]
    korni = []
    for t in ts:
        if t >= 0:
            x = math.sqrt(t)
            korni.append(x)
            korni.append(-x)
    return korni
def vyvesti(korni):
    if len(korni) == 0:
        print("Корней нет")
        return
    unikalnye = []
    for k in korni:
        if k not in unikalnye:
            unikalnye.append(k)
    print("Корни:")
    for k in unikalnye:
        print("x =", round(k, 4))
a = vvesti("A")
b = vvesti("B")
c = vvesti("C")
print("Уравнение:", a, "x^4 +", b, "x^2 +", c, "= 0")
korni = poschitat(a, b, c)
vyvesti(korni)