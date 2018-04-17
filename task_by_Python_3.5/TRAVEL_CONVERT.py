import osa


def convert_to_kilometres(miles):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    response = client.service.ChangeLengthUnit(miles, 'Miles', 'Kilometers')
    return response


def file_to_list():
    with open('travel.txt') as file:
        return convert_to_kilometres(sum(
            [float(i.split()[1].replace(',', '')) for i in file]))

print('Длина пути: {:.2f}'.format(file_to_list()), 'километр(а)(ов).')
