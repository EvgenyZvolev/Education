# Открытие web-сайта
import os
sayt = input('Введите адрес сайта: ')
if 'https://' in sayt:
    os.system('start '+ sayt)
elif 'www.' in sayt:
    sayt = 'https://' + sayt
    os.system('start '+ sayt)
else:
    sayt = 'https://www.' + sayt
    os.system('start ' + sayt)
