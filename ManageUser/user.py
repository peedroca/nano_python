def create(users):
    username = input("What username to user? ")
    fullname = input("And what the name? ")
    age = int(input("ok ... how old are your user? "))
    users[username] = [fullname, age]


def list_users(users):
    print(users)
    for key, user in users.items():
        print(key.rjust(12, ".") + ":", user[0].rjust(15, " ") + " " + str(user[1]))


def remove_user(username, users):
    del(users[username])


def save_on_file(filename, users):
    with open(filename + ".txt", 'r+') as file:
        file.truncate(0)

    with open(filename + ".txt", "a") as file:
        for key, user in users.items():
            file.write(key.rjust(12, ".") + ": " + user[0].rjust(15, " ") + " " + str(user[1]) + "\n")
