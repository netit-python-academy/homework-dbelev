import sys

A = input('Enter  price A:')
B = input('Enter price B:')
C = input('Enter price C:')
words = input('Enter number of words:')


try:
    A = float(A)
    B = float(B)
    C = float(C)
    words = int(words)
except:
    print('Not a number')
    sys.exit()

if not (0.02 <= A <= 0.89 and 0.02 <= B <= 0.89 and 0.02 <= C <= 0.89):
    print('Must be between 0.02 and 0.89')
    sys.exit()

delta = 0
if words <= 20:
    print(f'{A + B}')
else:
    delta = words - 20
    print(f'{A + B + delta*C}')


