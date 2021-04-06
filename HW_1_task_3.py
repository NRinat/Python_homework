number = int(input('Введите число от 0 до 20 '))

if number == 1:
    end = 'процент'
elif 2 <= number <= 4:
    end = 'процента'
elif number > 20:
    end = 'больше запрашиваемого числа'
else:
    end = 'процентов'

print(number, end)
