number = 23
guess = int(input('ВВедите целое число: '))

if guess == number:
    print ('Вы угадали число')
if guess < number:
    print('Загаданное число немного больше')
else:
    print('Загаданное число немного меньше')
