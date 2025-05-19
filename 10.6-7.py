#10.6-7

class Dog :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def 멍멍(self):
        print('my_dog의 이름은{}이고 나이는 {}살입니다.'.format(self.name, self.age))

    def __str__(self):
        return '이름은'+self.name+'이고 나이는 '+self.age+'살입니다'


my_dog = Dog('Mango', '3')

my_dog.멍멍()


print(my_dog)
