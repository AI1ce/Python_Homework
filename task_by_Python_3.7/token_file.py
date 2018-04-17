from pprint import pprint
import requests

APP_ID = 'c16fafeebb1e4addbb42bf39b6697796'
URL = 'https://oauth.yandex.ru/authorize'
auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}
# print('?'.join((URL, urlencode(auth_data))))
TOKEN = 'AQAAAAAEyByLAASnBxESKIDfYECemfDbTfZRkcM'


def get_counters(token):
    headers = {
        'Authorization': 'OAuth {}'. format(token),
        'Content-Type': 'application/x-yametrika+json'
}
    management_url = 'https://api-metrika.yandex.ru/management/v1/counters'
    response = requests.get(management_url, headers=headers)
    return response.json()
counters = get_counters(TOKEN)
pprint(counters)
