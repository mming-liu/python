# 第一题
# class Apple:
#     def __init__(self,w,l,c,we,):
#         self.width = w
#         self.lenth = l
#         self.color = c
#         self.weight = we
#         print("the apple size is %d , color is %s,weight is %d"%(w*l,c,we))
#
# x = Apple(1,2,'blue',3)
# print(x)

#第二题，圆的面积
# from math import pi
#
# class Circle:
#     def __init__(self,r):
#         '''
#         第三题用到新建一个类方法，所以第二题还是使用__init__
#         '''
#         self.radius = r
#         r = float(r)
#         area = pi * pow(r,2)
#         print(area)
#
# x = Circle(input("请输入圆的半径："))
# print(x)

# 第三题,三角形面积
# class Triangle:
#     def area(self,base,height):
#         self.base = base
#         self.height = height
#         area = 0.5 * base * height
#         return area
#
# Triangle = Triangle()    #创建对象
# x = Triangle.area(1,2)
# print(x)

#第四题，正六边形的周长
class Hexagon:
    def cacculate_perimeter(self,side):
        self.side = side
        perimeter = 6 * side
        return perimeter

Hexagon = Hexagon()
x = Hexagon.cacculate_perimeter(3)
print(x)