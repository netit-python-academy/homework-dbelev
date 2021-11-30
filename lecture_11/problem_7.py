import sys
import math

point1 = (3, -5)
point2 = (-3, 3)
point3 = (-1, -2)


a = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 )
b = math.sqrt((point2[0] - point3[0])**2 + (point2[1] - point3[1])**2 )
c = math.sqrt((point1[0] - point3[0])**2 + (point1[1] - point3[1])**2 )

print(a,b, c)

if a == b == c:
    print("Равнобедрен")
elif (a == b or b == c):
    print("Равностранен")
else:
    print("Разностранен")

