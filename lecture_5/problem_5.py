import sys


a = input('Enter one side:')
b = input('Enter second side:')

try:
    a = int(a)
    b = int(b)
except:
    print('Not a number')
    sys.exit()

if a == b:
    print(f'Квадрат, лице {a*b} , периметър {(a + b)*2}')
else:
    print(f'лице {a * b} , периметър {(a + b)*2}')
