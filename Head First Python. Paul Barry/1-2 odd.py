#Gregory Pereverzev 11.11.2019
#Вторая (модифицированная первая) программа из книги.

from datetime import datetime
#from time
import time
from random import randint

#Создаем список нечетных минут:
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

#Запускаем цикл 5 раз:
for i in range(0, 5):
    #Присваиваем переменной right_this_minute значение текущей минуты:
    right_this_minute = datetime.today().minute
    #Проверяем значение переменной на нахождение в списке:
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    #Запускаем таймер с помощью функции sleep (принимаемый аргумент равен количесиву секунд, функция randint(a, b)
    #генерирует число от a до b):
    time.sleep(randint(1, 60))