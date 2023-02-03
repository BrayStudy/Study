import string
import random
import sys
import time

granted = False


def main():
    menu()


def menu():
    global option
    print("Welcome to our Simple Login Application!")
    print()

    option = input("""
A: Register
B: Login
Q: Quit Program

Please enter your choice: """)
    if option == "A" or option == "a":
        access('register')
    elif option == "B" or option == "b":
        access('login')
    elif option == "Q" or option == "q":
        time.sleep(2)
        sys.exit()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()


def grant():
    global granted
    granted = True


def login(name, password):
    success = False
    file = open("accounts.txt", "r")
    for i in file:
        if i.strip() == "":
            continue
        a, b = i.split(" ")
        b = b.strip()
        if (a == name and b == password):
            success = True
            break
    file.close()
    if (success):
        print("Logged in.")
        grant()
    else:
        print("Wrong Username or Password")


def register(name, password):
    file = open("accounts.txt", "a")
    file.write("\n" + name + " " + password)
    file.close()
    print("Registered.")
    grant()


def access(option):
    global name
    if (option == "login"):
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        login(name, password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your username: ")
        pass_gen = input("Do you want a generated password? yes/no: ")
        if pass_gen.lower() == "yes":
            password = get_random_pw()
        else:
            password = input("Enter your password: ")
        register(name, password)


def get_random_pw():
    length = int(input("Enter password length: "))

    print('''Choose character set for password from these :
            1. Digits
            2. Letters
            3. Special characters
            4. Exit''')

    characterList = ""

    while (True):
        choice = int(input("Pick a number "))
        if (choice == 1):

            characterList += string.ascii_letters
        elif (choice == 2):

            characterList += string.digits
        elif (choice == 3):

            characterList += string.punctuation
        elif (choice == 4):
            break
        else:
            print("Please pick a valid option!")

    password = []

    for i in range(length):

        randomchar = random.choice(characterList)

        password.append(randomchar)

    print("The random password is " + "".join(password))

    return "".join(password)
main()
if (granted):
    print("Welcome")
    print(name)
