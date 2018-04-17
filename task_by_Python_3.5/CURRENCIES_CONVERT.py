import osa


def file_to_list():
    with open('currencies.txt') as file:
        for_line_in_file = file.readlines()
    for_line_in_file = [i.strip().split(' ') for i in for_line_in_file]
    return(for_line_in_file)


def currencies_convert(from_conv, in_conv):
    client = osa.client.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    response = client.service.ConvertToNum(toCurrency='RUB',
                                           fromCurrency=from_conv,
                                           amount=in_conv,
                                           rounding=True)
    return(response)


def rubles(currency):
    rubles_only = []
    for course in currency:
        rubles_only.append(currencies_convert(course[2], course[1]))
    return(rubles_only)

amount_in_rubles = round(sum(rubles(file_to_list())))
print('Сумма, потраченная на билеты: ', amount_in_rubles, 'рублей(ля)(ль).')
