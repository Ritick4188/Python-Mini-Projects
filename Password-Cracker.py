import string
from random import *

# Enter Your Password in Lowercase and Lowlength


def crack_password():
    user_pass = input('Enter Your Password : ')
    password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    guess = ''

    while guess != user_pass:
        guess = ''
        for letter in range(len(user_pass)):
            guess_letter = password[randint(0,25)]
            guess = str(guess_letter) + str(guess)

            print(guess)

    print('Your Password is :', guess)


crack_password()
