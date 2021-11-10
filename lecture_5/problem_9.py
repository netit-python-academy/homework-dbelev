import sys

X1 = input("Enter X1:")
Y1 = input("Enter Y1:")
X2 = input("Enter X2:")
Y2 = input("Enter Y2:")

try:
    X1 = int(X1)
    Y1 = int(Y1)
    X2 = int(X2)
    Y2 = int(Y2)
except:
    print('Enter valid numbers!')
    sys.exit()

if not (5 <= X1 <= 100 or 5 <= X2 <= 100 or 5 <= Y1 <= 100 or 5 <= Y2 <= 100):
    print('Numbers must be between 5 and 100! Exiting...')
    sys.exit()

if X1 < X2:
    if Y1 < Y2 or X1 < Y2:
        print('Вместват се')
elif X1 > X2:
    if X2 > Y2 or X2 > Y1:
        print('Вместват се')
else:
    print('Не се вместват')

    
    

