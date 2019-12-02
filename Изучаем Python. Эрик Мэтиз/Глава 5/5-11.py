#Gregory Pereverzev 24.10.2019

list = []

for x in range(1, 10):
    list.append(x)

for x in list:
    if x == 1:
        print(str(x) + "st")
    elif x == 2:
        print(str(x) + "nd")
    elif x == 3:
        print(str(x) + "rd")
    else:
        print(str(x) + "th")

