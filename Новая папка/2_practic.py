# print(bool(3.4)) true
bool(-150)
bool(0)
bool(' ')
bool('')
# a = input('Введите что угодно: ')
# if a:
#    print('Ok')
a = "строка"
b = "число"
c = a > b
print(c)
c = len(a) > len(b)
print(c)
# Практическое задание 2
# 1. Точка с координатами (x, y) находится в первой или во второй четверти, и не дальше чем
# 3 см. от начала координат.
x = float(input("Input x: "))
y = float(input("Input y: "))
if -3 <= x <= 3 and 0 <= y <= 3:
    print("точка принадлежит области")
else:
    print("точка не принадлежит областей")

# 2. Среди чисел x, y, z есть равные, и хотя бы одно из чисел x или y четно.
z = float(input("Input z: "))
if x == y or x == z or y == z or x % 2 == 0 or y % 2 == 0:
    print("Среди чисел x, y, z есть равные, и хотя бы одно из чисел x или y четно is true")
else:
    print("Среди чисел x, y, z есть равные, и хотя бы одно из чисел x или y четно is false")
# 3. Число x принадлежит отрезку[2,5] или [-1,1].
if 2 <= x <= 5 or -1 <= x <= 1:
    print("x принадлежит какой-то из областей")
else:
    print("х не принадлежит никакой из области")

# 4. Точка с координатами (x, y) находится снаружи квадрата со стороной 1 ,левый нижний
# угол которого находится в начале координат
if (x < 0 or x > 1) and (y < 0 or y > 1):
    print("Точка находится вне квадрата")
else:
    print("Точка находится внутри квадрата")
# 4
candy = 17
iceCream = 70
money = int(input("Сколько денег: "))
if candy + iceCream > money:
    print("Недостаточно")
else:
    print("Оплачено")

# Практическое задание 3
# Ввести координаты двух отрезков числовой оси и определить, пересекаются ли они.
a = float(input("input a: "))
b = float(input("input b: "))
a1 = float(input("input a1: "))
b1 = float(input("input b1: "))
if a == a1 and b == b1:
    print("отрезки совпадают")
elif (a < a1 and a < b1 and b < a1 and b < b1) or (a > a1 and a > b1 and b > a1 and b > b1):
    print("отрезки не пересекаются")
else:
    print("отрезки пересекаются")
# Практическое задание 4
age = int(input('Ваш возраст: '))
print('Рекомендовано:', end=' ')
# 4.1. Напишите эффективную реализацию кода с помощью elif и контролем введенных данных.
Age = 0
while 18 > Age or Age > 100:  # Контроль возраста
    Age = int(input("Ваш возраст: "))  # Будем спрашивать, пока не введут подходящий возраст
print("Рекомендовано:", end=" ")
if 18 <= Age <= 26:
    print("Активный комплекс")
elif 26 < Age <= 40:
    print("Силовые нагрузки ")
elif 40 < Age <= 60:
    print("Общефизическая подготовка")
else:
    print("Лечебная физкультура")

# 4.2. Задание теста содержит 60 вопросов, за которые может быть получено 60 баллов.
# Необходимо конвертировать в привычную шкалу оценок: 0-24: неуд.,
# 25-36: удовл., 37-48: хорошо, 49-60: отлично.
# Предусмотреть случай, когда введены числа, не входящие в заданные диапазоны
point = -1
mark = 2
while point < 0 or point > 60:
    point = int(input("Write your points: "))
if 0 <= point <= 24:
    mark = 2
elif 24 < point <= 36:
    mark = 3
elif 36 < point <= 48:
    mark = 4
elif 48 < point <= 60:
    mark = 5
print("your mark is ", mark)

# 5
try:
    n = input("Введите целое число: ")
    n = int(n)
    print("Yes")
except ValueError:
    print("No")
try:
    a = float(input("Введите делимое: "))
    b = float(input("Введите делитель: "))
    c = a / b
    print("Частное: %.2f" % c)
except ValueError:
    print("Введена строка")
except ZeroDivisionError:
    print("Деление на ноль")
# 5.1. Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться конкатенация строк,
# иначе введенные числа суммируются. Пример вывода: Первое значение: 1 Второе значение: 5.5
# Результат: 6.5 Или Первое значение: abc Второе значение: 9 Результат: abc9
# Подсказка: можно использовать извлечение типа.e
a = input("Введите первое значение: ")
b = input("Введите второе значение: ")

try:
    a = float(a)
except ValueError:
    a = a

try:
    b = float(b)
except ValueError:
    b = b

if type(a) == str or type(b) == str:
    try:
        a = str(a)
    except ValueError:
        pass

    try:
        b = str(b)
    except ValueError:
        pass

c = a + b
print("c =", c)
# 5.2. Напишите код, который позволит определить, содержит ли введенное значение только цифры от 0 до 9.
value = input("Input value: ")
try:
    value = float(value)
    print("Only numbers")
except ValueError:
    value = value
    print("No only numbers or no numbers")
