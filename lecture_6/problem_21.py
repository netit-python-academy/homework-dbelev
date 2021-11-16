for i in range(1,8):
    for j in range(1,6):
        if i == 1 or i == 2 or i == 5 or i == 6 or i == 7:
            if j == 1 or j == 5:
                print('*', end='')
            else:
                print(' ', end='')
        elif i == 3:
            if j != 3:
                print('*', end='')
            else:
                print(' ', end='')
        elif i == 4:
            if j != 2 and j != 4:
                print('*', end='')
            else:
                print(' ', end='')
    print()