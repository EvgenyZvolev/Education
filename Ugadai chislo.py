import random
name = input("Введите Ваше имя: ")
print("Здравствуй, " + name + '! Сыграем с тобой в игру "Угадай число!"\nПопробуй отгадать число от 1 до 5, которое я загадал!')
while True:
   random_number = random.randint(1, 5)
   user_number = input("Введите число от 1 до 5: ")
   if int(user_number) != random_number:
      print("Число неверное! Было загадано число: " + str(random_number) + ". Попробуй ещё раз!")
   elif int(user_number) == random_number:
      print(name + ", ты красавчик! :) Число угадано верно!")
      break
