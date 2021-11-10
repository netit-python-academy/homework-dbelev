budget = int(input())
category = input()
people = int(input())

if people > 0 and people <= 4:
    transport = budget * 0.75
elif people > 4 and people <= 9:
    transport = budget * 0.6
elif people > 9 and people <=24:
    transport = budget * 0.5
elif people > 24 and people <=49:
    transport = budget * 0.40
elif people > 49 and people <=200:
    transport = budget * 0.25
else:
    print('Number of people out of range')
    exit()

if category == 'VIP':
    price = people * 499.99
    change = budget - price - transport
elif category == 'Normal':
    price = people * 249.99
    change = budget - price - transport
else:
    print('category unknown')
    exit()

if change >= 0:
    print(f'Yes! You have {change:.2f} leva left')
else:
    change = change * -1
    print('Not enough money!You need {change:.2f} leva')   
