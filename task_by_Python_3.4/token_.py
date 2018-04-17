from urllib.parse import urlencode

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6214146
VERSION = '5.68'

params = {
    'client_id': APP_ID,
    'display': 'page',
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'scope': 'friends',
    'response_type': 'token',
    'v': VERSION
}

if __name__ == '__main__':
    print('?'.join((AUTHORIZE_URL, urlencode(params))))