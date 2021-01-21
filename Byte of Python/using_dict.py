ab ={
'Swaroop' : 'swaroop@swaroopch.com',
'Larry' : 'larry@wall.org',
'Matsumoto' : 'matz@ruby-lang.org',
'Spammer' : 'spammer@hotmail.com'
}

print(ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']

print('\nв адрксной книге {0} контакта\n'.format(len(ab)))

# метод items() класса dict - возвращает список кортежей, каждый из которых
# содержит пару элементов: ключ и значение
for name, address in ab.items():
    print('контакт - {0}, адрес - {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

# Проверить, существует ли пара ключ-значение, можно при помощи оператора in
if 'Guido' in ab:
    print('адрес guido', ab['Guido'])

