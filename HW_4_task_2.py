import requests

currency_request = input('Введите код валюты')
'''Наименование валюты вводится на основаннии международной кваллификации состоящей из трех заглавных латинских букв'''


def currency_rates(char_code):
    char_code = char_code.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    response = response.split('</Valute>')
    currency_dict = {}
    for i in response:
        code = i[i.find('CharCode') + 9:i.find('CharCode') + 12]
        value = i[i.find('Value') + 6:i.find('Value') + 13]
        currency_dict[code] = value
    print(currency_dict.get(char_code, None))


currency_rates(currency_request)


