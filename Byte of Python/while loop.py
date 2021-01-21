number = 23
running = True

while running:
    guess = int(input('ВВедите целое число: '))
    if guess == number:
        print ('Вы угадали число')
        running = False
    elif guess < number:
        print('Загаданное число немного больше')
    else:
        print('Загаданное число немного меньше')
else:
    print('цикл While закончен')

print('Exit')
