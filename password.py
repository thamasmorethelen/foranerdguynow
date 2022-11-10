from password_genny import password_generator


def user_num():
    user_input = ''
    while True:
        try:
            user_input = int(input('Please enter an integer greater than 12: '))
            return user_input
        except ValueError:
            input('Please enter an number greater than 12')


# Function that contains main while loop
def app():
    num = 0
    while num < 12:
        num = user_num()
    print(password_generator(num))


if __name__ == '__main__':
    app()
