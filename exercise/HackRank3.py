# import numpy as np
#
# l = []
# u = []
# m = [[0 for i in range(3)] for i in range(3)] #创建一个3*3的矩阵
# row, col = 0, 1 #初始行列设置01的位置
# num = 1
# while num <= 9:
#     m[row][col] = num #先将01放到第一行中间位置
#     num += 1 #每一次循环数字加一
#     row -= 1 #下一位数字的行下标
#     col += 1 #下一位数字的列下标
#     if row < 0 and col >= 3: #判断超出上方行，右方列
#         row, col = row + 2, col - 1
#     elif row < 0: #判断只有行超出上方行
#         row = 3 - 1
#     elif col >= 3:#判断只有行超出右方列
#         col = 0
#     elif m[row][col] != 0:   #判断下一位不为初始值0
#         row, col = row + 2, col - 1
# #按照列表中存储的数字打印出来
# print(m)


# import sys
#
# n = int(input())
# dict = {}
# for i in range(n):
#     keyValue = input().split()
#     key = str(keyValue[0])
#     value = str(keyValue[1])
#     dict[key] = value
#
# # stopword = ""
# # names = []
# # for line in iter(input, stopword):
# #     names.append(line)
#
# lines = sys.stdin.readlines()
# names = []
# for i in lines:
#     line = i.rstrip('\n').strip()
#     names.append(line)
#
# # names = [str(e) for e in input().split()]
# print(names)
#
# for m in names :
#     try:
#         print(m+'='+dict[m])
#     except KeyError:
#         print('Not Found')

# 继承
# class Person:
#     def __init__(self, firstName, lastName, idNumber):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.idNumber = idNumber
#     def printPerson(self):
#         print("Name:", self.lastName + ",", self.firstName)
#         print("ID:", self.idNumber)
#
# class Student(Person):
#     def __init__(self,firstName, lastName, idNum,scores):
#         super().__init__(firstName, lastName, idNum)
#         self.avg = 0
#         sumScore = 0
#         for i in range(len(scores)) :
#             sumScore = scores[i] + sumScore
#             self.avg = sumScore/len(scores)
#
#     def calculate(self):
#         if self.avg >= 90 and self.avg <= 100:
#             return 'O'
#         elif self.avg >= 80 and self.avg < 90:
#             return 'E'
#         elif self.avg >= 70 and self.avg < 80:
#             return 'A'
#         elif self.avg >= 55 and self.avg < 70:
#             return 'P'
#         elif self.avg >= 40 and self.avg < 55:
#             return 'D'
#         else :
#             return 'T'
#
# # Heraldo Memelli 8135627
# # 2
# # 100 80
# line = input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input()) # not needed for Python
# scores = list( map(int, input().split()) )
# s = Student(firstName, lastName, idNum, scores)
# s.printPerson()
# print("Grade:", s.calculate())


#抽象类
# from abc import ABCMeta, abstractmethod
# class Book(object, metaclass=ABCMeta):
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     @abstractmethod
#     def display(self): pass
#
# class MyBook(Book):
#     def __init__(self,title,author,price):
#         super().__init__(title,author)
#         self.price = price
#
#     def display(self):
#         print('Title:',self.title)
#         print('Author:',self.author)
#         print('Price:',self.price)
#
# #And Then There Were None
# #Agatha Christie
# #448

# title=input()
# author=input()
# price=int(input())
# new_novel=MyBook(title,author,price)
# new_novel.display()



# class Difference:
#     def __init__(self, a):
#         self.__elements = a
#
#     def computeDifference(self):
#         self.a = a
#         self.different = 0
#         self.differents = []
#         for m in range(len(a)):
#             for n in range(len(a)-1):
#                 if m != n+1:
#                     self.different = abs(a[m]-a[n+1])
#                     self.differents.append(self.different)
#                     self.differents = list(set(self.differents))
#
#         self.maximumDifference = max(self.differents)
#
# _ = input()
# a = [int(e) for e in input().split(' ')]
#
# d = Difference(a)
# d.computeDifference()
#
# print(d.maximumDifference)


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Solution:
#     def display(self,head):
#         current = head
#         while current:
#             print(current.data,end=' ')
#             current = current.next
#
#     def insert(self,head,data):
#         node=Node(data)
#         if head==None:
#             head=node
#         else:
#             pre=head
#             while pre.next:
#                 pre=pre.next
#             pre.next=node
#         return head
#
# mylist= Solution()
# T=int(input())
# head=None
# for i in range(T):
#     data=int(input())
#     head=mylist.insert(head,data)
# mylist.display(head);



# class Calculator:
#     def __init__(self):
#         # self.n = n
#         # self.p = p
#         pass
#
#     def power(self,n,p):
#         self.n = n
#         self.p = p
#         e = 'n and p should be non-negative'
#         if n >= 0 and p >=0 :
#             result = pow(n,p)
#             return result
#         else:
#             return e
#
# myCalculator=Calculator()
# T=int(input())
# for i in range(T):
#     n,p = map(int, input().split())
#     try:
#         ans=myCalculator.power(n,p)
#         print(ans)
#     except Exception as e:
#         print(e)




class Solution:
    def __init__(self):
        self.size = len(s)
        self.stack = []
        self.top = -1
        self.front = -1
        self.rear = -1
        self.queue = []
    def pushCharacter(self, strr):
        if self.isfull_stack():
            raise Exception("stack is full")
        else:
            self.stack.append(strr)
            self.top = self.top + 1

    def popCharacter(self):
        if self.isempty_stack():
            raise Exception("stack is empty")
        else:
            self.top = self.top - 1
            last = self.stack.pop()
            return last

    def isfull_stack(self):
        return self.top + 1 > self.size

    def isempty_stack(self):
        return self.top == -1

    def show_stack(self):
        return self.stack

    def enqueueCharacter(self, strr):
        if self.isfull_queue():
            raise Exception("queue is full")
        else:
            self.queue.append(strr)
            self.rear = self.rear + 1

    def dequeueCharacter(self):
        if self.isempty_queue():
            raise Exception("queue is empty")
        else:
            first = self.queue.pop(0)
            self.front = self.front + 1
            return first

    def isfull_queue(self):
        return self.rear - self.front + 1 > self.size

    def isempty_queue(self):
        return self.rear == self.front

    def show_queue(self):
        return self.queue

s=input()
obj=Solution()

l=len(s)
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")