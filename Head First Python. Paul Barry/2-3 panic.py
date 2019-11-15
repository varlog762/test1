#Gregory Pereverzev 15.11.2019

phrase = 'Don\'t panic!'
plist = list(phrase)
print(phrase)
print(plist)

list0 = ['o', 'n', ' ', 't', 'a', 'p']
list1 = []

for ch in phrase:
    if ch in list0:
        if ch not in list1:
            list1.append(ch)
print(list1)


new_phrase = ' '.join(plist)
print(plist)
print(new_phrase)