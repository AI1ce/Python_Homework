import subprocess
import os

def get_list(source):
    return [photo for photo in os.listdir('Source') if '.jpg' in photo.lower()]

def new_photo(source_folder, new_folder):
    if new_folder not in os.listdir():
        os.mkdir(new_folder)    
    for photo in get_list(source_folder):
        source_photo = os.path.join(source_folder, photo)
        new_photo = os.path.join(new_folder, photo)
        subprocess.Popen(['convert', source_photo, '-resize', '200', new_photo])   

if __name__ == "__main__":
    source_folder = 'Source'
    new_folder = 'Result'
    new_photo(source_folder, new_folder)