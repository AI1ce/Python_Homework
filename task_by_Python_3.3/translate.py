import os
import requests

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

def translate_it(text, multitranslation):
    r = requests.get(URL, params={'key': KEY, 'lang': multitranslation, 'text': text}).json()
    return ' '.join(r.get('text', []))

print('Пожалуйста, подождите, программа производит перевод. \nПерейдите в текущую директорию, чтобы использовать результат перевода в папке "russian".')


if __name__ == '__main__':
    lang = 'ru'
    if 'russian' not in os.listdir():
        os.mkdir('russian')
    for all_multilang_file in os.listdir('multilanguage'):
        multilang_file = os.path.join('multilanguage', all_multilang_file)
        with open(multilang_file, 'r', encoding='UTF8') as f:
            lang_m = all_multilang_file[:-4].lower()
            translation = translate_it(f.read(), '{}-{}'.format(lang_m, lang))
            fnl_file = os.path.join('russian', all_multilang_file)
            with open(fnl_file, 'w', encoding='UTF8') as f:
                f.write(translation)
