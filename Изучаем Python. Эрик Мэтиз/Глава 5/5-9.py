#Gregory Pereverzev 23.10.2019

users = ["admin", "Gregory", "Eugenia", "Andrew", "Slavik"]

if users:
    for user in users:
        if user.lower() == "admin":
            print("Hello, admin! Would you like to see a status report?")
        else:
            print("Hello, " + user.title() + "!")
else:
    print("We need find some users!")

users = []

if users:
    for user in users:
        if user.lower() == "admin":
            print("\nHello, admin! Would you like to see a status report?")
        else:
            print("\nHello, " + user.title + "!")
else:
    print("\nWe need find some users!")