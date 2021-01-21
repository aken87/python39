from zipfile import ZipFile
import os
import time

# фнкция для получения всех файлов и каталогов, принимает аргумент (папку которую будет сканировать)
def get_all_file_paths(directory):
    
    # пустой лист для путей
    file_paths = []

    # сканирование каталогов и подкаталогов
    
    # Функция walk() модуля os принимает один аргумент - имя каталога
    # Возвращает объект, из которого получают кортежи для каждого каталога переданного каталога.
    for root, directories, files in os.walk(directory):  
        for filename in files:
            filepath = os.path.join(root, filename) # получает все пути и объединяет 
            file_paths.append(filepath)             # добавляет все пути в список file_path из filepath

    # возвращение всех путей файлов       
    return file_paths

def main():
    # путь к папке которую нажно архивировать
    directory = 'C:\My Documents'

    today = time.strftime('%Y_%m_%d')

    now = time.strftime('%H-%M-%S')

    target = today + os.sep + now + '.zip'
    
    # вызываем функцию для получения путей файлов из директории directory
    file_paths = get_all_file_paths(directory)

    print('Список файлов:')
    for file_name  in file_paths:
        print(file_name )

    with ZipFile(target, 'w') as zip:
        for file in file_paths:
            zip.write(file)      
    print('Резервная копия успешно создана в', target)
        
if __name__ == "__main__": 
    main() 
