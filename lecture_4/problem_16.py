month = input()
number_nights = int(input())


if month == 'May' or month == 'October':
    studio = number_nights * 50
    apartment = number_nights * 65
    if number_nights > 7 and number_nights < 14:
        studio = studio - studio*0.05
    if number_nights > 14:
        studio = studio - studio * 0.3
if month == 'June' or month == 'September':
    studio = number_nights * 75.2
    apartment = number_nights * 68.7
    if number_nights > 14:
        studio = studio - studio * 0.2

if month == 'July' or month == 'August':
    studio = number_nights * 76
    apartment = number_nights * 78

if number_nights > 14:
    apartment = apartment - apartment * 0.1


print(f'Apartment: {apartment:.2f} leva')
print(f'Studio: {studio:.2f} leva')