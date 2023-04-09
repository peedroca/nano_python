from user import *

def show_menu():
    return input("Select an option:\n" +
                 "<C> Create an user\n" +
                 "<D> Delete an user by username\n" +
                 "<L> List users\n" +
                 "<G> Get users from txt\n" +
                 "<S> Save users on txt\n" +
                 "<E> Exit\n")


menuOption = show_menu().upper()
users = {}
while menuOption != 'E':
    if menuOption == 'C':
        create(users)
    elif menuOption == 'D':
        remove_user(input("What username do you want to remove? "), users)
    elif menuOption == 'L':
        list_users(users)
    elif menuOption == 'S':
        save_on_file("users", users)
    # elif menuOption == 'G':

    menuOption = show_menu().upper()
