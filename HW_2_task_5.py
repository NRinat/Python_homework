price = [57.8, 46.51, 97, 0.6, 104.44, 87.2, 9.99, 13.5, 99.22, 0.11]
print('Native_id->', id(price))

price.sort()
print(price)
print('Sort_id->', id(price))

price_reversed = list(sorted(price))
print(list(reversed(price)))
print('Reversed_id->', id(list(reversed(price))))

b = []
i = 0
max_in = 0
time = 0
while i < len(price):
    b.append(max(price))
    max_in = price.index(max(price))
    del price[max_in]
    time += 1
    if time == 5:
        break
print('Five_expensive:', b)


