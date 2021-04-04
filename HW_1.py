time = input('Введите время в секундах')
sec = int(time)
minute = int(time) / 60
hour = int(time) / 3600
day = int(time) / 86400
month = int(time) / 2592000
if int(time) >= 60:
    sec = int(time) % 60
else:
    sec = int(time)
if int(time) >= 60 and int(time) < 3600:
    minute = int(time) / 60
else:
    minute = 0
if int(time) >= 3600 and int(time) < 86400:
    hour = int(time) / 3600
else:
    hour = 0
if int(time) >= 86400 and int(time) < 2592000:
    day = int(time) / 86400
else:
    day = 0
if int(time) >= 2592000:
    month = int(time) / 2592000
else:
    month = 0
print(int(month), 'месяц', (day), 'день', int(hour), 'час', int(minute), 'минута', sec, 'секунда')