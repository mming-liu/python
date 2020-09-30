# from decimal import Decimal
# from math import pi
#
# class shape:
#     def what_am_i (self):
#         print('I am a shape')
#
# class Rectangle(shape):
#     def calculate_perimeter(self,s1,s2):
#         self.s1 = s1
#         s1 = Decimal(s1)
#         self.s2 = s2
#         s2 = Decimal(s2)
#         return 2 * (s1+s2)
#
# class Square(shape):
#     def calculate_perimeter(self,r):
#         self.r = r
#         return 2 * pi * r
#
#     def change_size(self,size):
#         self.size = size
#         size = float(size)
#         if size < 0 :
#             size = abs(size)
#         else :
#             size = abs(size) + 1
#         return size
#
# Rectangle = Rectangle()
# Rectangle.what_am_i()
# x = input('Type a number:')
# y = input('Type another:')
# print(Rectangle.calculate_perimeter(x,y))
#
# Square = Square()
# Square.what_am_i()
# r = Square.change_size(input('input a number:'))
# print(r)
# print(Square.calculate_perimeter(r))

# class House:
#     def house(self,owner,name):
#         self.owner = owner
#         self.name = name
#         print("%s's owner is %s"%(name,owner))
#
# class Rider:
#     def rider(self,name):
#         self.name = name
#         return name
#
# Rider = Rider()
# House = House()
# x = Rider.rider('Jack')
# House.house(x,'kaer')

class House :
    def __init__(self,owner,name):
        self.owner = owner
        self.name = name

class Rider:
    def __init__(self,name):
        self.name = name

x = Rider('Jack')
y = House(x,'kaer')
print(y.owner.name)

