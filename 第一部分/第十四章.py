# class Square:
#     square_list = []
#
#     def __init__(self,r):
#         self.r = r
#         self.square_list.append(self.r)
#
# square = Square(1)
# square = Square(1)
# square = Square(1)
# square = Square(1)
# print(square.square_list)

# class Square:
#     def __init__(self,size):
#         self.size = size
#
#     def print_size(self):
#         print('{} by {} by {} by {}'.format(self.size,self.size,self.size,self.size))
#         print('%s by %s by %s by %s '%(self.size,self.size,self.size,self.size))
#
# square = Square(29)
# square.print_size()

class Same :
    def same(self,name):
        self.name = 'liu'

same = Same()
same_name = same
print(same_name is same)

different = Same()
print(different is same)