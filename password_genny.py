import random
import string

# password generator as a function
def password_generator(num):
    password = []
    while len(password) < int(num):
        choice = random.choice(string.printable)
        if choice not in string.whitespace:
            password.append(choice)
    return ''.join(password)


class Password_Generator:
    def generate(self):
        password = []
        while len(password) < 15:
            choice = random.choice(string.printable)
            if choice not in string.whitespace:
                password.append(choice)
        return ''.join(password)
