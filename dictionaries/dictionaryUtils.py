def create(dictionary):
    name = input('Inform username: ')
    fullname = input('Inform fullname: ')
    age = int(input('How old are you? '))
    dictionary[name] = [fullname, age]


def search_by_username(username, dictionary):
    return dictionary.get(username)


def remove_by_username(username, dictionary):
    del(dictionary[username])
