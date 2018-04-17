import os

migrations = 'Migrations'
current_directory = os.path.dirname(os.path.abspath(__file__))

def search_word(file_name, word, abs_way):
    with open(os.path.join(abs_way, file_name), 'r', encoding='cyrillic') as f:
        return word in f.read()

def files_reader(abs_way):
    all_files = os.listdir(abs_way)
    return [file_name for file_name in all_files if '.sql' in file_name]

def search_files(files_list, word, abs_way=''):
    new_files_list = []
    for file_name in files_list:
        if search_word(file_name, word, abs_way):
            new_files_list.append(file_name)
    return new_files_list

if __name__ == '__main__':
    abs_way = os.path.join(current_directory, migrations)
    files = files_reader(abs_way)
    while True:
        word = input('Введите строку: ')
        files = search_files(files, word, abs_way)
        print('\n'.join(files))
        result_len = len(files)
        print('Всего: {}'.format(result_len))
      