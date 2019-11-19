#Gregory Pereverzev 15.11.2019 - 19.11.2019

phrase = 'Don\'t panic!'
plist = list(phrase)
print(phrase)
print(plist)

new_plist = plist[1:3]
new_plist.extend(plist[4:8])
new_plist.insert(-2, new_plist.pop())
new_plist.insert(2, new_plist.pop(-2))

new_phrase = ' '.join(new_plist)
print(plist)
print(new_phrase)