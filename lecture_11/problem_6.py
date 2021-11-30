import math
from typing import Sequence
point1 = (-3, -4)
point2 = (4, 5)




delta = (point1[0] - point2[0], point1[1] - point2[1])

needle = math.sqrt(delta[0]**2 + delta[1]**2)

print(f"The distance beween these ponts is:{needle:.10f}")
