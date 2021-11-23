'''
student_scores = {
 "John": [100, 90, 80],
 "Bob": [100, 70, 80]
}
'''

student_scores = {
 "Susan": [67, 84, 75, 63],
 "Mike": [87, 98, 64, 71],
 "Jim": [90, 58, 73, 86]
}


a =0

for key, value in student_scores.items():
    b = 0
    for i in value:
        b += int(i)
    if a < b:
        a = b
        name = key

print(name)
    
