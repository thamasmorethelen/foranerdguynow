# Password Generator a program
import string
import random
from password_genny import password_generator
# Function that captures user input
def user_num():
    user_input = ''
    while True:
        try:
            user_input = int(input('Please enter an integer greater than 10: '))
            return user_input
        except ValueError:
            input('Please enter an integer (whole number) greater than 10')


# Function that contains main while loop
def app():
    num = 0
    while num < 10:
        num = user_num()
    print(password_generator(num))


if __name__ == '__main__':
    app()
