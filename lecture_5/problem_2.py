import sys

a = input('Enter two digit number:')
b = input('Enter second number:')

if (len(a) != len(b) or len(a) != 2):
    print("Error! Must be 2 digit number!")
    sys.exit()


try:
    a = int(a)
    b = int(b)
except:
    print('Enter valid numbers!')

multi = a * b

last = int(str(multi)[-1])

if last % 2 == 0:
    check_even = 'четно'
else:
    check_even = 'нечетно'

print(f'{multi}, {last} {check_even}')


    




