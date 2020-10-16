# import sys
#
# # Complete the compareTriplets function below.
# def compareTriplets(a, b):
#     sum1 = 0
#     sum2 = 0
#     sum = []
#     i = 0
#
#     array = a + b
#     for m in array:
#         if m < 0 or m>100 :
#             print('type numbers range 0 to 100')
#             sys.exit()
#
#     while i <= len(a)-1 :
#         if a[i] < b[i] :
#             sum2 += 1
#         elif a[i] > b[i] :
#             sum1 += 1
#         else :
#             sum1 += 0
#             sum2 += 0
#         sum = [sum1,sum2]
#         i += 1
#     print(sum)
#
#
# if __name__ == '__main__':
#     a = list(map(int, input().rstrip().split()))
#     b = list(map(int, input().rstrip().split()))
#     result = compareTriplets(a, b)

# import sys
#
# # Complete the aVeryBigSum function below.
# def aVeryBigSum(ar):
#     i = 0
#     sum = 0
#     if ar_count < 1 or ar_count > 10 :
#         print('array length is rang 1 to 10')
#         sys.exit()
#
#     while i < ar_count :
#         if ar[i] < 0 or ar[i] > 10 ** 10 :
#             print('the elements are rang 0 to 10^10')
#             sys.exit()
#         else :
#             sum = sum + ar[i]
#         i += 1
#
#     print(sum)
#
# if __name__ == '__main__':
#     ar_count = int(input())
#     ar = list(map(int, input().rstrip().split()))
#     result = aVeryBigSum(ar)

# 多维数组的两条对角线数字之和的差
# def diagonalDifference(arr):
# # Write your code here
#     x = 0 ; y = 0;sum1 = 0;sum2 =0
#     for x in range(n) :
#         for y in range(n) :
#             if x == y :
#                 sum1 = sum1 + arr[x][y]
#
#     for x in range(n) :
#         for y in range(n) :
#             if x + y == n-1:
#                 sum2 = sum2 + arr[x][y]
#
#     return abs(sum1 - sum2)
#
# if __name__ == '__main__':
#     n = int(input().strip())
#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#     result = diagonalDifference(arr)
#     print(result)

# 打印#组成的三角形
# def staircase(n):
#     for i in range(n):
#         print(' '*(n-i-1)+'#'*(i+1))
#
# if __name__ == '__main__':
#     n = int(input())
#     staircase(n)

# def birthdayCakeCandles(candles):
#     max_height = max(candles)
#     count = 0
#     for i in candles :
#         if max_height == i :
#             count += 1
#     return count
#
# if __name__ == '__main__':
#     candles_count = int(input().strip())
#     candles = list(map(int, input().rstrip().split()))
#     result = birthdayCakeCandles(candles)

# 12小时制时间转换成24小时制
# def timeConversion(s):
#     hh = s[0:2]
#     mm = s[3:5]
#     ss = s[6:8]
#     apm = s[8:]
#     print(hh,mm,ss,apm)
#     if hh == '12' and apm.__contains__('AM'):
#         hh = '00'
#         print('%s:%s:%s'%(hh,mm,ss))
#     elif hh == '12' and apm.__contains__('PM'):
#         print(s[0:8])
#     elif apm == 'AM' :
#         print(s[0:8])
#     else :
#         hh = str(int(hh)+12)
#         print('%s:%s:%s'%(hh,mm,ss))
#
# if __name__ == '__main__':
#     s = input()
#     result = timeConversion(s)

# def beautifulDays(i, j, k):
#     '''
#     从i到j之前，i与i的相反数之差的绝对值，可以整除k的数字个数：
#     ：i，起始数
#     ：j,结束数
#     ：k，除数
#     '''
#     count = 0
#     while i <= j :
#         if abs(i - reverse(i)) % k == 0 :
#             count += 1
#         i += 1
#     return count
#
# def reverse(i) :
#     #构造i的相反数
#     i = str(i)
#     i = reversed(i)
#     i = ''.join(i)
#     return int(i)
#
# if __name__ == '__main__':
#     ijk = input().split()
#     i = int(ijk[0])
#     j = int(ijk[1])
#     k = int(ijk[2])
#     result = beautifulDays(i, j, k)
#     print(result)
import os


# def gradingStudents(grades):
#     '''
#     :当输入值小于38时，直接输出
#     :当输入值大于38且与比输入值大的5的倍数的差大于等于3时，直接输出
#     :当输入值大于38且与比输入值大的5的倍数的差小于3时，输出5的倍数
#     '''
#     list = []
#     for grade in grades :
#         big_grade = (grade // 5 + 1) * 5
#         if grade < 38 or big_grade - grade >= 3:
#             grade = grade
#         else:
#             grade = big_grade
#         list.append(grade)
#     return list
#
# if __name__ == '__main__':
#     grades_count = int(input().strip())
#     grades = []
#     for _ in range(grades_count):
#         grades_item = int(input().strip())
#         grades.append(grades_item)
#     result = gradingStudents(grades)
#     result = '\n'.join(map(str,result))
#     print(result)

# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     '''
#     功能：计算a+apples[i]和b+oranges[i]在s,t范围内的数字数量
#     s:起始数值
#     t:终止数值
#     a:apples的起点值
#     b:oranges的起点值
#     apples:apple运动的距离
#     Oranges:orange运动的记录
#     '''
#     count_apples,count_oranges = 0,0
#     for apple in apples :
#         new_apple = apple + a
#         # new_apples.append(new_apple)
#         if new_apple <= t and new_apple >= s :
#             count_apples += 1
#     print(count_apples)
#
#     for orange in oranges :
#         new_orange = orange + b
#         # new_oranges.append(new_orange)
#         if new_orange <= t and new_orange >= s :
#             count_oranges += 1
#     print(count_oranges)
#
#     # return count_apples,count_oranges
#
# if __name__ == '__main__':
#     st = input().split()
#     s = int(st[0])
#     t = int(st[1])
#     ab = input().split()
#     a = int(ab[0])
#     b = int(ab[1])
#     mn = input().split()
#     m = int(mn[0])
#     n = int(mn[1])
#     apples = list(map(int, input().rstrip().split()))
#     oranges = list(map(int, input().rstrip().split()))
#     result = countApplesAndOranges(s, t, a, b, apples, oranges)

# def reverse_words_order_and_swap_cases(sentence):
#     # Write your code here
#     '''
#     字符串数组前后位置翻转，并改变大小写
#     '''
#     s1 = sentence.split(' ')
#     s1.reverse() #数组翻转函数
#     s1 = ' '.join(s1)
#     s2 = ''
#
#     for a in s1:
#         if 65 <= ord(a) <= 90 :
#             a = chr(ord(a) + 32)
#         elif 97 <= ord(a) <= 122:
#             a = chr(ord(a) - 32)
#         else :
#             a = a
#         s2 = s2 + a
#     print(s2)
#
# if __name__ == '__main__':
#     sentence = input()
#     result = reverse_words_order_and_swap_cases(sentence)