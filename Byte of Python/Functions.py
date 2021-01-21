def say():
    print('hello world')

# значения указаные в объявлении функции называются – параметрами
def maxNumber(a,b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

maxNumber(4,3)

x = 5
y = 7

# значения которые передаются в функцию при её вызове называются – аргументами
maxNumber(x,y)

print(f(say(a,b)))
