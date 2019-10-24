#Gregory pereverzev 23.10.2019

current_users = ["admin", "gashek", "Atomzerg", "Eugenia", "SLAVAK"]
new_users = ["admin", "ZAZA", "goblin", "Atomzerg", "August"]

for new_user in new_users:
    '''#print(new_user)
    new_user = new_user.lower()
    print(new_user)
    for current_user in current_users:
        current_user = current_user.lower()
        print(current_user)'''
    if new_user in current_users:
        print(new_user + " zaniato!")
    else:
        print("Welcome " + new_user + "!")
