# def fizzBuzz(n):
#     # Write your code here
#     i = 1
#     while (i <= n):
#         if (i % 3 ==0 and i % 5 ==0):
#             print('FizzBuzz')
#             i = i + 1
#         elif (i % 3 != 0 and i % 5 == 0):
#             print('Buzz')
#             i = i + 1
#         elif (i % 3 ==0 and i % 5 != 0):
#             print('Fizz')
#             i = i + 1
#         else :
#             print(i)
#             i = i + 1
#
# if __name__ == '__main__':
#     n = int(input().strip())
#     fizzBuzz(n)

#!/bin/python3
#
# import math
# import random
# import re
# import sys
#
#
# class Car:
#     def __init__(self,max_speed, speed_unit):
#         self.max_speed = max_speed
#         self.speed_unit = speed_unit
#
#     def __str__(self):
#         return 'Car with the maximum speed of %d %s'%(max_speed,speed_unit)
#
# class Boat:
#     def __init__(self,max_speed):
#         self.max_speed = max_speed
#
#     def __str__(self):
#         return 'Boat with the maximum speed of %d'%(max_speed)
#
# if __name__ == '__main__':
#     q = int(input())
#     queries = []
#     for _ in range(q):
#         args = input().split()
#         vehicle_type, params = args[0], args[1:]
#         if vehicle_type == "car":
#             max_speed, speed_unit = int(params[0]), params[1]
#             vehicle = Car(max_speed, speed_unit)
#             print(vehicle)
#         elif vehicle_type == "boat":
#             max_speed = int(params[0])
#             vehicle = Boat(max_speed)
#             print(vehicle)
#         else:
#             raise ValueError("invalid vehicle type")


def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    s1 = sentence.split(' ')
    s1.reverse() #数组翻转函数
    s1 = ' '.join(s1)
    s2 = ''
    print(s1)

    for a in s1:
        if 65 <= ord(a) <= 90 :
            a = chr(ord(a) + 32)
        elif 97 <= ord(a) <= 122:
            a = chr(ord(a) - 32)
        else :
            a = a
        s2 = s2 + a
    print(s2)

if __name__ == '__main__':
    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)