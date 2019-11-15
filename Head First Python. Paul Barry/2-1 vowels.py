#Gregory Pereverzev 15.11.2019
#Проверяем содержаться ли в слове гласные из списка.

#Объявляем список гласных.
vowels = ['a', 'e', 'i', 'o', 'u']
#
word = 'Milliways'

for letter in word:
    if letter in vowels:
        print(letter)
