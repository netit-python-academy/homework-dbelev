import random
number = random.randint(1,1000)

guess = 0
while number != guess:
    guess = int(input('Guess a number:'))
    if guess > number:
        print('Too high')
    elif guess < number:
        print('Tool low')
print('Correct!')


