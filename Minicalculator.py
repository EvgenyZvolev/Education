name = input ('Введите Ваше имя: ')
print ('Hello, ' + name + '! Вашему вниманию представлен мини калькулятор.' )
x = 0
while x < 4:
    x += 1
    a = float(input ('Введите первое число: '))
    znak = input ('Введите знак действия: ')
    b = float(input ('Введите второе  число: '))
    if znak == "+":
        s = float(a + b)
    elif znak == "-":
        s = float (a - b)
    elif znak == "/":
        s = float (a / b)
    elif znak == "*":
        s = float (a * b)
    print ('Ответ равен: ' + str(s))

print ('Программа завершена')
