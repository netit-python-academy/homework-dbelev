dimension = 21
while dimension > 20:
    dimension = int(input('Въведете число по-малко от 20:'))

for i in range(1,dimension+1):
    for j in range(i,dimension+i):
        print(j, end='')
    print()