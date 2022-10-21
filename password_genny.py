import random
import string

# password generator as a function
def password_generator():
    password = []
    while len(password) < 15:
        choice = random.choice(string.printable)
        if choice not in string.whitespace:
            password.append(choice)
    return ''.join(password)


print('Printed as a Function:')
print(password_generator())

class Password_Generator:

    def generate(self):
        password = []
        while len(password) < 15:
            choice = random.choice(string.printable)
            if choice not in string.whitespace:
                password.append(choice)
        return ''.join(password)
gen = Password_Generator()

print("Printed as a class:")
print(gen.generate())