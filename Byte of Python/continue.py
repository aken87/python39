while True:
    s = input('напишите что нибудь:')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало символов')
        continue
    print('Длина строки:', len(s))
print('Exit')
