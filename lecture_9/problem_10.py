scrab = {
    1: ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: "K",
    8: ["J", "X"],
    10: ["Q", "Z"]
    }

word = input("Write a word with uppercase:")

est = 0
for i in word:
    for key, value in scrab.items():
        if i in value:
            est += key

print(est)

