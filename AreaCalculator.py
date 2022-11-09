'''
This program will automate the process for
calculating the area of either a circle or a trianle.
'''

print('The program is beginning!')

name = input('What is your name? ')
option = input("Enter 'C' or Circle or 'T' for Trianle: ").upper()
while option != 'T' or option != 'C':
    if option == 'C':
        try:
            radius = float(input('What is the radius: '))
        except ValueError:
            radius = float(input('This time please enter a number: '))
        area = 3.14159 * radius**2
        print('The area is {:.2f}'.format(area))
        break
    elif option == 'T':
        try:
            base = float(input('Please enter the base of the triangle: '))
        except ValueError:
            base = float(input('This time please enter a number: '))
        try:
            height = float(input('Please enter the height of the trianle: '))
        except ValueError:
            height = float(input('This time please enter a number: '))
        area = 0.5 * base * height
        print('The trianles area is {:.2F}'.format(area))
        break
    else:
        print("Oh no! Please enter 'T' or 'C'")
        option = input("Enter 'C' or Circle or 'T' for Trianle: ").upper()

print("Thanks for using our area calculator!")
