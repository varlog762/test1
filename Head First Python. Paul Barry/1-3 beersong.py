#Gregory Pereverzev 13.11.2019
#Третья программа из книги.

word = "bottles"

for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer jn the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it arround.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")