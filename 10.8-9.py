#10.8-9

class Counter:
    def __init__(self, number=0):
        if number > 100 or number < -1:
            self.__number = 0
        else:
            self.__number = number

    def reset(self):
        self.__number = 0

    def inc(self):
        self.__number += 1
        if self.__number > 100:
            self.__number = 0

    def dec(self):
        self.__number -= 1
        if self.__number < -1:
            self.__number = 0

    def __str__(self): 
        return "C({})".format(self.__number)

    def __add__(self, other):
        print('__add__')
        return self.__number + other.__number
    def __sub__(self, other):
        print('__sub__')
        return self.__number - other.__number

c1 = Counter(10)
c1.inc()
print('c1 =', c1)


#10.9
c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print('c3 =', c3)
print('c4 =', c4)
