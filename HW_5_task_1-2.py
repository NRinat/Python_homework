from itertools import islice


def odd_nums(max_value):
    n = -1
    while n <= max_value - 1:
        n += 2
        yield n


odd_to_15 = odd_nums(15)
print(next(odd_to_15))

print(*islice(odd_to_15, 15))

max_val = 15
odd_nums_gen = (n for n in range(1, max_val + 1, 2))

print(next(odd_nums_gen))

print(*islice(odd_nums_gen, 15))
