import json

files = [
    {'name': 'newsafr.json', 'encoding': 'utf-8'},
    {'name': 'newscy.json', 'encoding': 'koi8_r'},
    {'name': 'newsfr.json', 'encoding': 'cyrillic'},
    {'name': 'newsit.json', 'encoding': 'cp1251'},
]

if __name__ == '__main__':

    for news_block in files:
        with open( news_block['name'], 'r',
                   encoding=news_block['encoding'] ) as file:
            news = json.load(file)

        words = {}
        for item in news['rss']['channel']['items']:
            for word in item['description'].split():
                if len(word) > 6:
                    word = word.lower()
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1

        words_sorted_keys = sorted(words, key=words.get, reverse=True)
        print('\n{:-^30}'.format(news_block['name']))
        for number, word in enumerate(words_sorted_keys[:10]):
            print('{:>2}. {}'.format(number+1, word))