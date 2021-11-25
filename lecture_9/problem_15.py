customers = {
 "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
 "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
}
min_price = 10
min_orders = 3


estimate = {}
for key, value in customers.items():
    counter = 0
    for i in value:
        if min_price <= i:
            counter+=1
    estimate[key] = counter

result=[]
for k, v in estimate.items():
    if v >= min_orders:
        result.append(k)

print(result)