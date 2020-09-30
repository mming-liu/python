'''
# 输入一个数字，输出平方(float类型计算结果不准确)
from _decimal import Decimal, InvalidOperation

def sqe(a):
    try:
        a = Decimal (a)
        a = a ** a
    except (ValueError,InvalidOperation):
        print("请输入数字")

sqe(input("type a number:"))

#构造一个3个必选参数，2个可选参数的函数
def parameter (a,b,c,d=1,e=2):
    sum = a+b+c+d+e
    print(sum)

parameter(4,5,6,7,8)

#编写一个带两个函数的程序。第一个函数应接受一个整数为参数，并返回该整数
#除以 2 的值。第二个函数应接受一个整数作为参数，并返回该整数乘以 4 的值。调用第
#一个函数，将结果保存至变量，并将变量作为参数传递给第二个函数。
import sys
b=0
def divide(a):
    try:
        a = int(a) // 2
        global b
        b = a
        print(a)
        print(b)
    except (TypeError,ValueError):
        print("请输入整数")
        sys.exit()

def time(c):
    global b
    c = 4 * b
    print(c)

time(divide(input("输入一个整数：")))
'''
#编写一个将字符串转换为 float 对象并返回该结果的函数。使用异常处理来捕获
#可能发生的异常
def transfor(a):
    try :
        float(a)
        print(a)
    except ValueError:
        print("请输入数字")

transfor(input("请输入字符串："))