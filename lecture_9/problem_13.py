words = ["HaPPy", "mOOdy", "yummy", "mayBE"]

output = {}
for word in words:
    i = 0
    for letter in word:
        if letter.isupper():
            i+=1
    if i in output:
        output[i] = [output[i], word]
    else:
        output[i] = word

print(output)


