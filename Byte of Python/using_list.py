shopList = ['хлеб','молоко','овощи','мясо']

print('я должен сделать', len(shopList), 'покупок')

print('покупки:',end=' ')
for i in shopList:
    print(i, end=' ')

    
# метод append() для класса list - добавление в список
shopList.append('рис')
print('\nтеперь список такой', shopList)

# метод sort() соритировка списка по умолчанию по алфавиту
shopList.sort()
print(shopList)

print('первое что нужно купить:', shopList[0])
lastitem = shopList[0]
del shopList[0]
print('я купил', lastitem)
print('осталовь купить', shopList)
