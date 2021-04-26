from collections import Counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    ip_address = []
    for line in f:
        new_line = line.split()
        ip_address.append(new_line[0])
        ip_address_counter = Counter(ip_address)
        max_num_spam = max(ip_address_counter.values())
        for key, value in ip_address_counter.items():
            if value == max_num_spam:
                print(f'{key}, количество запросов {value}')