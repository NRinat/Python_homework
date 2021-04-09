temperature = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
hour = 5
minute = 17
degree = 5

print(f'в "{hour:02}" часов "{minute:02}" минут температура воздуха была "+{degree:02}" градусов')

message = ' '.join(temperature)
print(message)





