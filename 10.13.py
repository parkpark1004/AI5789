#10.13

class Rectangle:
    def __init__(self, x , y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"Rectangle (x = {self.__x}, y = {self.__y}, w = {self.__width},h = {self.__height}), 면적 : {self.area()}"

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return self.__y
    
    def set_width(self, width): 
        self.__width = width  

    def get_width(self):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    def overlaps(self, r):
        if (self.__x < r.get_x() + r.get_width() and self.__x + self.__width > r.get_x() and
                self.__y < r.get_y() + r.get_height() and self.__y + self.__height > r.get_y()):
            return True
        else:
            return False

    def contains(self, r): 
        if (self.__x <= r.get_x() and self.__x + self.__width >= r.get_x() + r.get_width() and
                self.__y <= r.get_y() and self.__y + self.__height >= r.get_y() + r.get_height()):
            return True
        else:
            return False

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)

print('r1 contains r2 :', r1.contains(r2))
print('r1 contains r3 :', r1.contains(r3))
print('r1 overlaps r2 :', r1.overlaps(r2))
print('r1 overlaps r3 :', r1.overlaps(r3))
