def max (x, y):

    '''Выводит максимальное из двух чисел.
    Оба значения должны быть целыми числами.'''

    x = int(x)
    y = int(y)
    
    if x > y:
        print(x, 'наибольшее')
    elif x == y:
        print(y, 'наибольшее')

max(10,5)
print(max.__doc__)

help(max)
