# Основы программирования (Basics of programming)
# 1. Типы данных (переменных) (variables):
# int
number = 10
print(type(number))
# float
price = 10.5
print(type(price))
# str
name = 'Evgeny'
print(type(name))
# list
a = [1, 2, 'b']
print(type(a))
# tuple
a = (1, 2, 'b')
print(type(a))
# set
a = {1, 2, 'b'}
print(type(a))
# dict
a = {'a':1, 'b':2, 'c':3}
print(type(a))
# bool
status = True
print(type(a))
# NoneType
a = None
print(type(a))

# Действия со строками
# Конкатенация
print("\nHello, " + name + "!")
print("\nPrice = " + "$" + str(price))
# Экранирование
print("\nCode from the lock \"123456\"")
# f-str
name = 'Evgeny'
weather = 'облачно'
sum = 100.5
print(f"\nHello, {name}!")
print(f"Сейчас на улице {weather}, а у тебя в кармане ${sum}")

# 2. Математические операции:
# +, -, *, /, //, **, %, унарный минус, округление, Пи
a = 10
b = 3
print ("\nМатематические операции: +, -, *, /, //, **, %, унарный минус, округление, Пи:")
print ("Даны два числа. Первое равно 10, а второе равно 3")
sum = a + b
print(f"Сумма чисел равна: {sum} ")
raz = a - b
print(f"Разность чисел равна: {raz} ")
umn = a * b
print(f"Произведение чисел равно: {umn} ")
delen = a / b
print(f"Деление чисел равно: {delen} ")
delen_bez_ost = a // b
print(f"Деление чисел без остатка равно: {delen_bez_ost} ")
voz_v_step = a ** b
print(f"Возведение чисел в степень равно: {voz_v_step} ")
delen_po_mod = a % b
print(f"Деление чисел по модулю равно: {delen_po_mod} ")
print(f"Унарный минус числа 10 равен: " + str(-a))
c = 13.2
d = 13.7
print("Округление числа 13.2 равно: " + str(round(c)))
print("Округление числа 13.7 равно: " + str(round(d)))
# Импортируем модуль math:
import math
print("Округление числа 13.7 в меньшую сторону равно: " + str(math.floor(d)))
print("Округление числа 13.2 в большую сторону равно: " + str(math.ceil(c)))
print("Число Пи равно: " + str(math.pi))