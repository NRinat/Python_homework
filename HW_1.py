time = int(input('Введите время в секундах'))

second = time % 60
minute = time % 3600 // 60
hour = time % 86400 // 3660
day = time % 2592000 // 86400
month = time % 31104000 // 2592000
year = int(time / 31104000)

if second == 0:
   second = ''
else:
    second = f'{second} сек '

if minute == 0:
   minute = ''
else:
    minute = f'{minute} мин '

if hour == 0:
   hour = ''
else:
    hour = f'{hour} час '

if day == 0:
   day = ''
else:
    day = f'{day} день '

if month == 0:
   month = ''
else:
    month = f'{month} мес '

if year == 0:
   year = ''
else:
    year = f'{year} год '

print(f'{year}{month}{day}{hour}{minute}{second}')
