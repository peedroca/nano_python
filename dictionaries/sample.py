from dictionaryUtils import *

users = {}

create(users)
create(users)
print(users)

userFounded = search_by_username(input('What username are you searching? '), users)
print(userFounded)

remove_by_username(input('What username do you want to remove? '), users)
print(users)
