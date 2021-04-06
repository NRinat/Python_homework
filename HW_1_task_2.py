list_num = [i ** 3 for i in range(1001) if i % 2 == 1]

sum_num = 0
for i in list_num:
    sum_num_list = 0
    for j in str(i):
        sum_num_list += int(j)
    if sum_num_list % 7 == 0:
        sum_num += i

print(sum_num)