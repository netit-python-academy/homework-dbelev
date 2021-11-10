import sys


number = input('Please enter a tree digit number:')

if len(number) != 3:
    print('Not a 3 digits')
    sys.exit()

if '0' in number:
    print('Must not include 0')
    sys.exit

a = number[0]
b = number[1]
c = number[2]

try:
    number = int(number)
except:
    print('Not a number!')
    sys.exit()


if number % int(a) == 0 and number % int(b) == 0 and number % int(c) == 0:
    print('Дели се')
else:
    print('Не се дели')