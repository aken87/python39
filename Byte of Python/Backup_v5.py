import os
import time
import zipfile


print('Программа для создания резервных копий')
# указываем пути откуда брать и куда сохранять

# Указываю букву диска
source_name_drive = input ('Укажите букву диска:')

# К букве диска добавляется : и разделитель
source_drive_root = (source_name_drive + ':/')

# Указываем путь откуда будут копироваться файлы
source_user_path = input ('Укажите путь к папке ОТКУДА копировать ' + source_drive_root )

# Путь откуда будут браться файлы
source = source_drive_root + source_user_path

# указываем путь куда будут сохраняться
target_drive = input('Укажите букву диска для сохранения:')
target_drive_root = (target_drive + ':/')
target_user_path = input ('Укажите путь к папке КУДА сохранениять ' + target_drive_root )

# Корневая папка для бекапов
target_dir = target_drive_root + target_user_path
###########################################################################################

# Генерация имени для подкаталога
today = target_dir + os.sep + time.strftime('%Y_%d_%m')

# Генерация времени для архива 
now = time.strftime('%H-%M-%S')

# Комментарйи для архива
comment = input('заметка (можно оставить пустым):')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '(' + comment + ')' + '.zip'

# Генерация имени для архива текущая дата и время
target = today + os.sep + now + '.zip'

# Содание подкаталога если его нет
if not os.path.exists(today):               # Если нет каталога с именем из today
    os.mkdir(today)                         # Создать каталог с именем из переменной today
    print('Каталог создан в ', today)

z = zipfile.ZipFile(target, 'w')            # Создание нового архива
for root, dirs, files in os.walk(source):   # Список всех файлов и папок в директории source
    for file in files:
        z.write(os.path.join(root,file))    # Запись файлов в архив
        
        print('Обрабатываетя:', file)
        print(root)
        print('|---------------------------------------------|')
z.close()
print('Резервная копия успешно создана в', target)
