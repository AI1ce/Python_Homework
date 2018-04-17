import osa


def file_to_list():
    with open('temps.txt') as file:
        for_line_in_file = file.read().split('F')[:-1]
    for_line_in_file = [int(i.strip()) for i in for_line_in_file]
    return(for_line_in_file)


def temps_convert(Fahrenheit):
    client = osa.client.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    response = client.service.ConvertTemp(Temperature=Fahrenheit,
                                          FromUnit='degreeFahrenheit',
                                          ToUnit='degreeCelsius'
                                          )
    return(response)


def average_temps(F):
    avg_list_F = sum(F_temps) / (len(F_temps))
    return(avg_list_F)

F_temps = file_to_list()
avg_temps_F = average_temps(F_temps)
avg_temps_C = round(temps_convert(avg_temps_F))
print('Средняя температура за неделю: ', avg_temps_C, 'градус(ов) Цельсия')
