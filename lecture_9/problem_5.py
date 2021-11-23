d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'd':4}

delta = {}

for key in d1:
    if key in d2:
        if d1[key] != d2[key]:
            delta[key] = [d1[key], d2[key]]

for key in d1:
    if key not in d2:
        delta[key] = [None, d1[key]]

for key in d2:
    if key not in d1:
        delta[key] = [None, d2[key]]

print(delta)