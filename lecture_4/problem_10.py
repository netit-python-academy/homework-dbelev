dog_years = 10

if dog_years >= 2:
    man_years = 2*10.5 + (dog_years - 2)*4
elif dog_years == 1:
    man_years = 10.5
elif dog_years == 0:
    man_years = 0

print("This dog is at {} years".format(man_years))
