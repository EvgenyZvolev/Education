# Основы программирования (Basics of programming)
# 1. Типы данных (переменных) (variables):
# int (целое число)
number = 10
print(type(number))
# float (число с плавающей точкой)
price = 10.5
print(type(price))
# str (строка)
name = 'Evgeny'
print(type(name))
# list (список)
a = [1, 2, 'b']
print(type(a))
# tuple (кортеж)
a = (1, 2, 'b')
print(type(a))
# set (множество)
a = {1, 2, 'b'}
print(type(a))
# dict (словарь)
a = {'a':1, 'b':2, 'c':3}
print(type(a))
# bool (логическое булевое значение)
status = True
print(type(a))
# NoneType (отсутствие данных)
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

# 3.Условные операторы if, elif, else (Conditional operators)
# a)
if True:
    print('\n a) if')
elif True:
    print('elif')
else:
    print('else')
# b)
if False:
    print('if')
elif True:
    print('\n b) elif')
else:
    print('else')
# c)
if False:
    print('if')
elif False:
    print('elif')
else:
    print('\n c) else')

# 4. Оператор while
# a)
x = 0    #(переменная счетчика)
while x < 5:
    x += 1
    print (x)
else:
    print (x)
# b) Факториал числа 5!=1*2*3*4*5=120
x = 1
y = int(input('Введите число: '))
count = 0
while count < y:
    count += 1
    x *= count
print(x)
# с) для слова: 'hello'
x = ''
while len(x) < 5:
    y = input('Ввод данных: ')
    if y == 'o':
        continue  #(продолжение цикла)
    if y == 'l':
        break  #(завершение цикла)
    x += y
else:
    print(x)
print('Программа работат дальше')