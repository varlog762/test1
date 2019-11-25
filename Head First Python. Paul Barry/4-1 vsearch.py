#Gregory Pereverzev 25.11.2019
#Создаем первые функции.

def search4vowels(phrase:str) -> set:
    '''Возвращает гласные, найденные в указанной фразе.'''
    vowels = ser('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str) -> set:
    '''Возвращает множество букв из letters, найденное в указанной фразе.'''
    return set(letters).intersection(set(phrase))

#print(search4letters('fbviweo', 'v'))