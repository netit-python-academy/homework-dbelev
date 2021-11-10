N1 = int(input())
N2 = int(input())
operator = input()

if operator == '+' or operator == "-" or operator == '*' :
    if operator == '+':
        result = N1 + N2
    elif operator == '-':
        result = N1 - N2
    elif operator == '*':
        result = N1 * N2
    print('{0} {1} {2} = {3} -'.format(N1, operator, N2, result),"even " if result % 2 == 0 else 'odd')
if N2 !=0:
    if operator == '/':
        result = round(N1/N2, 2)
        print('{}/{}={}'.format(N1, N2, result))
    if operator == '%':
        result = N1 % N2 
        print('{} % {} = {}'.format(N1, N2, result))
else:
    print('Can not divide {} by zero'.format(N1))