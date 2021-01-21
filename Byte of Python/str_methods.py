# объект класса str
name = 'Nikita'

if name.startswith('Nik'):
    print('True')

# Оператор in используется для проверки,
# является ли некоторая строка частью данной строки
if 'a' in name:
    print('True')

if name.find('ta') != -1:
    print('True')

delimeter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimeter.join(mylist))
