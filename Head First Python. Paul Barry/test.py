def search4vowels():
    vowels = set('aeiou')
    word = input('Input your word:')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
