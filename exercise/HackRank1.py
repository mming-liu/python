# import sys
#
# def kangaroo(x1, v1, x2, v2):
#     '''
#     x1< x2，计算x1 是否能与x2在同一地点相遇，利用x1+ v1t = x2 + v2t 转换成t = (x2-x1)/(v1-v2)
#     比较t是否大于0，且是否为整数,除法结果为float型，与int之后的结果做比较
#     :param x1: x1的起点
#     :param v1: x1的速度
#     :param x2: x2的起点
#     :param v2: v2的速度
#     :return: 是否能相遇
#     '''
#     if x1 >= x2 :
#         print('x1 must smaller than x2')
#         sys.exit()
#
#     if v1 == v2 :
#         return 'NO'
#         sys.exit()
#
#     t = (x2 -x1)/(v1-v2)
#     if t > 0 and t == int(t):
#         return 'YES'
#     else:
#         return 'NO'
#
# if __name__ == '__main__':
#     x1V1X2V2 = input().split()
#     x1 = int(x1V1X2V2[0])
#     v1 = int(x1V1X2V2[1])
#     x2 = int(x1V1X2V2[2])
#     v2 = int(x1V1X2V2[3])
#     result = kangaroo(x1, v1, x2, v2)
#     print(result)


# def breakingRecords(scores):
#     count1,count2 = 0, 0
#     min,max = scores[0],scores[0]
#     for i in scores :
#         if i < min :
#             min = i
#             count2 += 1
#         if i > max :
#             max = i
#             count1 += 1
#     print(count1)
#     print(count2)
#
# if __name__ == '__main__':
#     n = int(input())
#     scores = list(map(int, input().rstrip().split()))
#     result = breakingRecords(scores)

# def birthday(s, d, m):
#     '''
#     数组s的元素，相邻的m个元素之后是否等于d
#     :param s: 数组
#     :param d: 需要的值
#     :param m: 步长
#     :return: 符合的组合数
#     '''
#     sum = 0
#     count = 0
#     for i in range(len(s)):
#         if m + i < len(s):
#             for x in range(i,m + i):
#                 sum = sum + s[x]
#
#         if sum == d :
#             count += 1
#         # sum置0，准备进行下一轮计算
#         sum = 0
#     print(count)
#
# if __name__ == '__main__':
#     n = int(input().strip())
#     s = list(map(int, input().rstrip().split()))
#     dm = input().rstrip().split()
#     d = int(dm[0])
#     m = int(dm[1])
#     result = birthday(s, d, m)

# def divisibleSumPairs(n, k, ar):
#     '''
#     数组中任意两个元素之和，是否能整除k
#     :param n: 数组长度
#     :param k: 除数
#     :param ar: 数组
#     :return: 符合条件的组合数
#     '''
#     count = 0
#     for x in range(n) :
#         if x <= n :
#             for y in range(x+1,n) :
#                 if (ar[x] + ar[y]) % k == 0 :
#                     count +=1
#     return count
#
# if __name__ == '__main__':
#     nk = input().split()
#     n = int(nk[0])
#     k = int(nk[1])
#     ar = list(map(int, input().rstrip().split()))
#     result = divisibleSumPairs(n, k, ar)
#     print(result)
import numpy as np


# def migratoryBirds(arr):
#     '''
#     打印出数组中出现次数最多的元素，当有多个元素出现次数相同时，返回下标最小的
#     :param arr: 数组
#     :return: 出现次数最多的元素
#     '''
#     # count = []
#     # for m in arr :
#     #     n = arr.count(m)
#     #     count.append(n)
#     #
#     # for n in count :
#     #     if n == max(count) :
#     #         x = count.index(n)
#     #         break
#     #
#     # return arr[x]
#
#     # return np.argmax(np.bincount(arr))
#
#     # 申明字典,通过for循环构造出一个有 元素：出现次数 的字典
#     appear_times = {}
#     for label in arr:
#         if label in appear_times:
#             appear_times[label] += 1
#         else:
#             appear_times[label] = 1
#
#     list = sorted(appear_times.items(),key=lambda x:x[0])
#     appear_times = dict(list)
#
#     most_common = max(appear_times, key=lambda x: appear_times[x])
#     return most_common
#
# if __name__ == '__main__':
#     arr_count = int(input().strip())
#     arr = list(map(int, input().rstrip().split()))
#     result = migratoryBirds(arr)
#     print(result)

# def dayOfProgrammer(year):
#     '''
#     判断是否是润年，并返回一年中的第256天是几月几号，1918是个特殊年份，1月31号后接2月14号
#     :param year: 年份
#     :return: 一年中的第256天是几月几号
#     '''
#     if year != 1918 :
#         if leap(year) == True:
#             print('12.09.%d'%year)
#         else:
#             print('13.09.%d'%year)
#     else:
#         print('26.09.%d'%year)
#
# def leap(year) :
#     if year >= 1918 :
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
#             return True
#         else:
#             return False
#     else :
#         if year % 4 == 0 :
#             return True
#         else:
#             return False
#
# if __name__ == '__main__':
#     year = int(input().strip())
#     result = dayOfProgrammer(year)

# def bonAppetit(bill, k, b):
#     sum = 0
#     for x in bill :
#         sum = sum + x
#     sum = int((sum -bill[k]) / 2)
#
#     if sum == b :
#         print('Bon Appetit')
#     else:
#         print(b - sum)
#
# if __name__ == '__main__':
#     nk = input().rstrip().split()
#     n = int(nk[0])
#     k = int(nk[1])
#     bill = list(map(int, input().rstrip().split()))
#     b = int(input().strip())
#     bonAppetit(bill, k, b)

def formingMagicSquare(s):
    sum1,sum2,count = 0,0,0
    s_a = []
    for m in range(3) :
        for n in range(3) :
            sum1 = sum1 + s[m][n]
            sum2 = sum2 + s[n][m]
        print(sum1,sum2)
        s_a.append(sum1)
        sum1 = 0
        sum2 = 0

    for n in s_a :
        count = count + abs(15-n)

    return count

if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
    print(result)