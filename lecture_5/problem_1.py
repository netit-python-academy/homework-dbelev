import sys

number = input('Enter a 4 digit number:')

try:
    number = int(number)
except:
    print('This is no number. Please enter a valid number!')
    sys.exit()

number = str(number)

if len(number) != 4:
    sys.exit('Error!Must be beween 1000 and 9999!')


first_number = int(number[0] + number[-1])
second_number = int(number[2] + number[3])

if first_number < second_number:
    print(f'По-малко ({first_number} < {second_number})')
elif first_number == second_number:
    print(f'равни ({first_number} = {second_number})')
else:
    print(f'По-голямо ({first_number} > {second_number})')

