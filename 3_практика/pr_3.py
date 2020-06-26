# Практическое задание 3 Напишите функцию main,
# в которой реализовано управление сценарием вызова всех написанных ранее функций.
from Head import division, nok


def main():
    a = float(input("Введите числитель первой дроби: "))
    b = float(input("Введите знаменатель первой дроби: "))
    c = float(input("Введите числитель второй дроби: "))
    d = float(input("Введите знаменатель второй дроби: "))
    try:
        a // b
    except ZeroDivisionError:
        b = 1
    try:
        c // d
    except ZeroDivisionError:
        d = 1

    a, b = division(a, b, c, d)
    if a == b:
        print(1)
    else:
        print(f"{a} / {b}")


main()
