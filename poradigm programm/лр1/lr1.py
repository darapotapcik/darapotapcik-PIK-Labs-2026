import math

while True:
    text = input("Введите A: ")
    try:
        a = float(text)
        break
    except ValueError:
        print("Это не число, попробуйте еще раз")

while True:
    text = input("Введите B: ")
    try:
        b = float(text)
        break
    except ValueError:
        print("Это не число, попробуйте еще раз")

while True:
    text = input("Введите C: ")
    try:
        c = float(text)
        break
    except ValueError:
        print("Это не число, попробуйте еще раз")

print("Уравнение:", a, "x^4 +", b, "x^2 +", c, "= 0")

D = b * b - 4 * a * c
print("Дискриминант =", D)

korni = []

if D < 0:
    print("Корней нет")
elif D == 0:
    t = -b / (2 * a)
    if t < 0:
        print("Корней нет")
    else:
        x1 = math.sqrt(t)
        korni.append(x1)
        korni.append(-x1)
else:
    t1 = (-b + math.sqrt(D)) / (2 * a)
    t2 = (-b - math.sqrt(D)) / (2 * a)
    if t1 >= 0:
        x1 = math.sqrt(t1)
        korni.append(x1)
        korni.append(-x1)
    if t2 >= 0:
        x2 = math.sqrt(t2)
        korni.append(x2)
        korni.append(-x2)
    if len(korni) == 0:
        print("Корней нет")

if len(korni) > 0:
    unikalnye = []
    for k in korni:
        if k not in unikalnye:
            unikalnye.append(k)
    print("Корни:")
    for k in unikalnye:
        print("x =", round(k, 4))