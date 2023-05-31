import os
import shutil
import unicodedata
import re
import sys

table = {ord(unicodedata.normalize('NFC', 'а')): 'a',
         ord(unicodedata.normalize('NFC', 'б')): 'b',
         ord(unicodedata.normalize('NFC', 'в')): 'v',
         ord(unicodedata.normalize('NFC', 'г')): 'h',
         ord(unicodedata.normalize('NFC', 'ґ')): 'g',
         ord(unicodedata.normalize('NFC', 'д')): 'd',
         ord(unicodedata.normalize('NFC', 'е')): 'e',
         ord(unicodedata.normalize('NFC', 'є')): 'ye',
         ord(unicodedata.normalize('NFC', 'ж')): 'zh',
         ord(unicodedata.normalize('NFC', 'з')): 'z',
         ord(unicodedata.normalize('NFC', 'и')): 'y',
         ord(unicodedata.normalize('NFC', 'і')): 'i',
         ord(unicodedata.normalize('NFC', 'ї')): 'yi',
         ord(unicodedata.normalize('NFC', 'й')): 'y',
         ord(unicodedata.normalize('NFC', 'к')): 'k',
         ord(unicodedata.normalize('NFC', 'л')): 'l',
         ord(unicodedata.normalize('NFC', 'м')): 'm',
         ord(unicodedata.normalize('NFC', 'н')): 'n',
         ord(unicodedata.normalize('NFC', 'о')): 'o',
         ord(unicodedata.normalize('NFC', 'п')): 'p',
         ord(unicodedata.normalize('NFC', 'р')): 'r',
         ord(unicodedata.normalize('NFC', 'с')): 's',
         ord(unicodedata.normalize('NFC', 'т')): 't',
         ord(unicodedata.normalize('NFC', 'у')): 'u',
         ord(unicodedata.normalize('NFC', 'ф')): 'f',
         ord(unicodedata.normalize('NFC', 'х')): 'kh',
         ord(unicodedata.normalize('NFC', 'ц')): 'ts',
         ord(unicodedata.normalize('NFC', 'ч')): 'ch',
         ord(unicodedata.normalize('NFC', 'ш')): 'sh',
         ord(unicodedata.normalize('NFC', 'щ')): 'shch',
         ord(unicodedata.normalize('NFC', 'ю')): 'yu',
         ord(unicodedata.normalize('NFC', 'я')): 'ya',
         ord(unicodedata.normalize('NFC', 'ь')): '',
         ord(unicodedata.normalize('NFC', 'А')): 'A',
         ord(unicodedata.normalize('NFC', 'Б')): 'B',
         ord(unicodedata.normalize('NFC', 'В')): 'V',
         ord(unicodedata.normalize('NFC', 'Г')): 'H',
         ord(unicodedata.normalize('NFC', 'ґ')): 'G',
         ord(unicodedata.normalize('NFC', 'Д')): 'D',
         ord(unicodedata.normalize('NFC', 'Е')): 'E',
         ord(unicodedata.normalize('NFC', 'Є')): 'Ye',
         ord(unicodedata.normalize('NFC', 'Ж')): 'Zh',
         ord(unicodedata.normalize('NFC', 'З')): 'Z',
         ord(unicodedata.normalize('NFC', 'И')): 'Y',
         ord(unicodedata.normalize('NFC', 'І')): 'I',
         ord(unicodedata.normalize('NFC', 'Ї')): 'Yi',
         ord(unicodedata.normalize('NFC', 'Й')): 'Y',
         ord(unicodedata.normalize('NFC', 'К')): 'K',
         ord(unicodedata.normalize('NFC', 'Л')): 'L',
         ord(unicodedata.normalize('NFC', 'М')): 'M',
         ord(unicodedata.normalize('NFC', 'Н')): 'N',
         ord(unicodedata.normalize('NFC', 'О')): 'O',
         ord(unicodedata.normalize('NFC', 'П')): 'P',
         ord(unicodedata.normalize('NFC', 'Р')): 'R',
         ord(unicodedata.normalize('NFC', 'С')): 'S',
         ord(unicodedata.normalize('NFC', 'Т')): 'T',
         ord(unicodedata.normalize('NFC', 'У')): 'U',
         ord(unicodedata.normalize('NFC', 'Ф')): 'F',
         ord(unicodedata.normalize('NFC', 'Х')): 'Kh',
         ord(unicodedata.normalize('NFC', 'Ц')): 'Ts',
         ord(unicodedata.normalize('NFC', 'Ч')): 'Ch',
         ord(unicodedata.normalize('NFC', 'Ш')): 'Sh',
         ord(unicodedata.normalize('NFC', 'Щ')): 'Shch',
         ord(unicodedata.normalize('NFC', 'Ю')): 'Yu',
         ord(unicodedata.normalize('NFC', 'Я')): 'Ya'}

extensions = dict(images=('jpeg', 'png', 'jpg', 'svg'),
                  video=('avi', 'mp4', 'mov', 'mkv'),
                  documents=('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'),
                  audio=('mp3', 'ogg', 'wav', 'amr'),
                  web=('html', 'xml', 'csv', 'json'),
                  archive=('zip', 'rar', 'gz', 'tar'),
                  other=())


def sort_files(path: str, path_: str) -> None:
    for file in os.listdir(path):
        if os.path.isfile(path + '\\' + file):
            process_file(path, file, path_)
        elif os.path.isdir(path + '\\' + file) and file.lower() not in extensions.keys():
            sort_files(path + '\\' + file, path_)


def process_file(path: str, file_name: str, root: str) -> None:
    current_path: str = path + '\\'
    *name, extension = file_name.split('.')
    for key, val in extensions.items():
        if extension in val:
            move_to(old_path=current_path, new_path=root + '\\' + key.title(), file_name='.'.join(name), ext=extension)
            break
        elif extension not in val and key == 'other':
            shutil.move(current_path + file_name, root + '\\' + key.title() + '\\' + file_name)


def check(path: str) -> None:
    for folder in os.listdir(path):
        if get_folder_size(path + '\\' + folder) == 0:
            shutil.rmtree(path + '\\' + folder)


def get_folder_size(folder_path: str) -> int:
    total_size: int = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


def rename(file_name: str) -> str:
    pattern = r'[\w\.\-\(\)]'
    for char in file_name:
        if not re.match(pattern, char):
            if ord(unicodedata.normalize('NFC', char)) in table.keys():
                new_char = char.translate(table)
                file_name = file_name.replace(char, new_char)
            else:
                file_name = file_name.replace(char, '_')
    return file_name


def move_to(old_path: str, new_path: str, file_name: str, ext: str) -> None:
    new_name: str = rename(file_name)
    if ext in extensions['archive']:
        try:
            os.makedirs('\\'.join((new_path, new_name.title())))
            shutil.unpack_archive(old_path + file_name + '.' + ext, '\\'.join((new_path, new_name.title())))
            os.remove(old_path + file_name + '.' + ext)
        except FileExistsError:
            os.remove(old_path + file_name + '.' + ext)
    else:
        os.rename(old_path + file_name + '.' + ext, old_path + new_name + '.' + ext)  # f'{old_path}{file_name}.{ext}'
        i: int = 0
        while True:
            if new_name + '.' + ext not in os.listdir(new_path):
                shutil.move(old_path + new_name + '.' + ext, new_path + '\\' + new_name + '.' + ext)
                break
            else:
                i += 1
                file_name = new_name
                new_name = file_name + f'_{i}'
                os.rename(old_path + file_name + '.' + ext, old_path + new_name + '.' + ext)
    if not os.listdir(old_path):
        os.rmdir(old_path)


def make_dir(path_to: str) -> bool:
    if os.path.exists(path_to):
        for key in extensions:
            try:
                os.makedirs('\\'.join((path_to, key.title())))
            except FileExistsError:
                continue
        return True
    else:
        print('Something went wrong. Check a validity of the entered path.')
        return False


def main():
    path = sys.argv[1]
    if make_dir(path):
        sort_files(path, path)
        check(path)


if __name__ == '__main__':
    main()
