class Robot:

    count = 0  # переменная класса
    
    def __init__(self, name):
        
        self.name = name
        print('инициализация:', self.name)
        Robot.count += 1

    def __del__(self):
        
        print('уничтожается:', self.name)
        Robot.count -= 1

        if Robot.count == 0:
            print(self.name, 'был последним')
        else:
            print('осталось', Robot.count)

    def say_hi(self):
        print('вас приветствует робот', self.name)

    def how_many():
        print('у нас {0:d} роботов'.format(Robot.count))

    how_many = staticmethod(how_many)

r1 = Robot('P0-i19')
r1.say_hi()
Robot.how_many()

r2 = Robot('C-3PO')
r2.say_hi()
Robot.how_many()

r3 = Robot('P-39UO')
r3.say_hi()
Robot.how_many()

print(Robot)
print(Robot.__init__)
print(Robot.how_many)
print(Robot.say_hi)
print(r1)
print(r2)

'''
1AD3E6B3 AF 0
1AD3E6B3 A6 0
1AD3E6B3 94 0
'''
