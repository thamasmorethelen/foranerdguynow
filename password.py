# Password Generator a program
import string
import random

# Function that captures user input
def user_num():
    user_input = ''
    while True:
        try:
            user_input = int(input('Please enter an integer greater than 10: ')) 
            return user_input
        except ValueError:
            input('Please enter an integer (whole number) greater than 10')


num = user_num()




# Function that contains main while loop
def app(num):
    password = []
    while len(password) < num:
        choice = random.choice(string.printable)
        if choice not in string.whitespace:
            password.append(choice)
    return ''.join(password)

print(app(num))
