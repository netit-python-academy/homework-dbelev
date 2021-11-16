import sys

N = 4
K = 3

a = b = 1

if N == K == 0:
    print('Невалиден вход')
    sys.exit()

if not (1 < K < N):
    print('K трябва да е по-малко от N')
    sys.exit()

for i in range(1,N+1):
    a *= i

for j in range(1,K+1):
    b *= j

print(a/b)
