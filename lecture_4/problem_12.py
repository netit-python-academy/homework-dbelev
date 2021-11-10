age = 33
sex = 'M'
family = 'Y'

if sex == 'F':
    print('She can work in the city')

if sex == 'M':
    if age >=20 and age <= 40:
        print('He can work anywhere')
    elif age > 40 and age < 60:
        print('He can work in the city')
    else:
        print('Error! Not allowed!')
