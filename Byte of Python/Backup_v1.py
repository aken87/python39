import os
import time

#https://docs.python.org/3/library/time.html#time.strftime

os.chdir(r'C:\Program Files (x86)\GnuWin32\bin')
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\My Documents"']

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'F:\\Backup' # Подставьте ваш путь.

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
target = target_dir + os.sep + time.strftime('%Y_%m_%d_%H-%M') + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
# метод jooin() класса str
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Ты думал здесь чтото будет? неееее')

