#Gregory Pereverzev 23.10.2019
users = ["admin", "Gregory", "Eugenia", "Andrew", "Slavik"]

for user in users:
    if user.lower() == "admin":
        print("Hello, admin! Would you like too see a status report?")
    elif user.lower() != "admin":
        print("Hello, " + user.title() + "!")