# 5.2. Напишите код, который позволит определить, содержит ли введенное значение только цифры от 0 до 9.
value = input("Input value: ")
try:
    value = float(value)
    print("Only numbers")
except ValueError:
    value = value
    print("строка содержит буквы или символы")