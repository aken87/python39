import os
import time
import zipfile

#https://docs.python.org/3/library/time.html#time.strftime

user_source = input('Укажите путь откуда копировать: ')

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = user_source # путь откуда будут копироваться файлы

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'F:\\Backup'       # корневая папка для бекапов

# 3. Файлы помещаются в zip-архив.
# 4. текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y_%d_%m') # генерация имени для подкаталога

# генерация времени для архива 
now = time.strftime('%H-%M-%S')

# комментарйи для архива
comment = input('заметка (можно оставить пустым):')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '(' + comment + ')' + '.zip' 

# содание каталога если его нет
if not os.path.exists(today):   #если нет каталога с именем из today
    os.mkdir(today)             #создать каталог с именем из переменной today
    print('Каталог создан в: ', today)

# 5. Используем команду "zip" для помещения файлов в zip-архив
# метод join() класса str
#zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

z = zipfile.ZipFile(target, 'w')            # Создание нового архива
for root, dirs, files in os.walk(source):   # Список всех файлов и папок в директории source
    for file in files:
        z.write(os.path.join(root,file))    # запись файлов в архив
        print('Обрабатываетя:', file)
        print(root)
        print('|---------------------------------------------|')
z.close()
print('Резервная копия успешно создана в', target)
