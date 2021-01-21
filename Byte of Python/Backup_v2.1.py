import os
import time
os.chdir(r'C:\Program Files (x86)\GnuWin32\bin')

#https://docs.python.org/3/library/time.html#time.strftime


# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\My Documents"'] # путь откуда будут копироваться файлы


# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'F:\\Backup'       # корневая папка для бекапов

# 3. Файлы помещаются в zip-архив.
# 4. текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y_%m_%d') # генерация имени для подкаталога

# генерация имени для зип архива с текущим временем
now = time.strftime('%H-%M-%S')

# содание каталога если его нет
if not os.path.exists(today):   #если нет каталога с именем из today
    os.mkdir(today)             #создать каталог с именем из переменной today
    print('Каталог успешно создан', today)

# имя для архива
target = today + os.sep + now + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
# метод join() класса str
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('ошибка')
