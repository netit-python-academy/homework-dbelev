competitors = {
 "Kate": 92,
 "Carol": 92,
 "Jess": 87,
 "Bruce": 87,
 "Scott": 84
 }

competitor_name = "Bruce"


rang = {}

estimate = list(competitors.values())
estimate.sort(reverse=True)

for k in competitors:
    position = estimate.index(competitors[k])
    rang[k] = position + 1

print(rang[competitor_name])



 