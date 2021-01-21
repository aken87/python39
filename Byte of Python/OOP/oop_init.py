class Person:

    def __init__(self, name):
        self.name = name
        
    def say_hi(self):
        print('привет', self.name)

p = Person('John')
p.say_hi()


print(type(p))
print(type(Person))
print(p)
