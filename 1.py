# int
number = 5
age = 22

# float
fnumber = 5.5

#str
name = "Alex"
name1 = 'Sam'

#bool
status = True
status = False

#список
list = []

#кортеж
turple = ()

#словарь
dict = {}

#экранирование \
print (" \"текст\" текст")

#перевод строки \n
print ("hello \nwordld")

#конкотенация
print ("имя " + name)
print ("ему " + str(age) + " года")
#---------------------------------------------------#


# метод format() для объединения строк
age = 20
name = 'Dan'
print('возраст {0} -- {1} лет.'.format(age,name))

# десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1/2))


# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{0:_^10}'.format('hell'))

#по улючевым словам
print('{name} написал {book}'.format(name='John', book='A byte of python'))
#---------------------------------------------------#


#input
#name = input("введите имя ")

#+, Сложение - Суммирует дваобъекта, 2 + 3 = 5, 'a' + 'b' = 'ab'
#-, Вычитание - Даёт разностьдвух чисел, 10 - 5 = 5, 50 - 26 = 24
#*, Умножение - Даёт произведение двух чисел или возвращает строку, повторённую заданное число раз, 2 * 3 = 6. 'la' * 3 = 'lalala'.
#/, Деление - Возвращает частное от деления x на y, 4 / 3 = 1.3333333333333333, 6 / 3 = 2
#**, Возведение в степень - Возвращает число х, возведённое в степень y, 3 ** 4 = 81, 4 ** 2 = 16
#%, Деление по модулю - остаток деления
#ceil-округление в большую сторону, pi-пи

import math

a = 5.65
print( math.floor(a))
print( math.ceil(a))
print( math.pi )
#---------------------------------------------------#

# Функция dir - возвращает список имён, определяемых объектом
import sys
dir(sys)
dir('print')
dir(str)
#---------------------------------------------------#

class <имя класса>:
    данные (атрибуты) - имена атрибутов существительные
    методы (функции) - имена методов называть глаголами

# Класс - это чертеж объекта

# Поля - переменные. Эти переменные/имена можно использовать только тогда,
# когда имеется объект этого класса.

# Методы - это функции внутри класса, определённые для использования только
# в этом классе.
# Этот функционал будет доступен только когда имеется объект данного класса

# Экземпляр класса - объект созданный из класса 

# Функция - это часть кода которую можно использовать многократно в любой части программы

# Параметры функции -  некоторые значения, передаваемые функции
# для того, чтобы она что-либо сделала с ними.
# Параметры указываются в скобках при объявлении функции и разделяются запятыми

# Аргументы функции - значения, которые вы передаёте в функцию при её вызове

# Объявление функции
def nameFunction():
    pass # Оператор pass используется в Python для обозначения пустого блока команд.
    return # Оператор return используется для возвратакаких то данных из функции

# Имена
long_name = 'Хорошее имя переменной'

# Имена классов
class MyFirstClass:

# имена констант
MAX_OVERFLOW = 10
TOTAL = 100

# Имена функций
my_variable = 'Variable'

# Циклы по спискам
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
    print(color)
    
# Циклы по списку чисел
for i in range(6):
    print(i**2)
    
# Импорты
import os
import sys



