#Gregory Pereverzev 23.10.2019

list0 = ["Eugenia", "Andrew", "Slavka", "Tolik"]
list1 = [1, 34, 435, 2, 7]
cat = "August"

print("If cat == 'August', it's good!")
if cat.lower() == "august":
    print('Good!')
print("If cat != 'August', it's bad!")
if cat != "udhvduivn":
    print("Bad!")

if "Eugenia" in list0:
    print("\nGood!")
else:
    print("Bad!")

if list1[1] > list1[3]:
    print("True")
else:
    print("False")

if 15 >= list1[0] and 32 <= list1[4]:
    print("False")
else:
    print("True")

if "Shura" not in list0:
    print("True")
