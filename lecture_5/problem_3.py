import sys

liters = input('Please eneter number:')

try: 
    liters=int(liters)
except:
    print('Not a number! Exiting...')
    sys.exit(1)

if not (10 <= liters <= 9999):
    print('Number must be between 10 and 9999')
    sys.exit(1)

buckets = liters // 5
remain = liters % 5

if (remain % 5 == 2):
    print(f'{buckets} пъти двете кофи и допълнително кофа от 2 литра')
elif (remain % 5 == 3):
    print(f'{buckets} пъти двете кофи и допълнително кофа от 3 литра')
elif remain % 5 == 1:
    print(f'{buckets -1} пъти двете кофи и допълнително две кофи от 3 литра')
elif remain % 5 == 4:
    print(f'{buckets -1} пъти двете кофи и допълнително две кофи от 2 литра')
elif remain % 5 == 0:
    print(f'{buckets} пъти двете кофи')

