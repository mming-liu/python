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
#
#     a = list(map(int, input().rstrip().split()))
#
#     b = list(map(int, input().rstrip().split()))
#
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

# 多维数组的两条对角线数字的差
def diagonalDifference(arr):
# Write your code here
    x = 0 ; y = 0;sum1 = 0;sum2 =0
    for x in range(n) :
        for y in range(n) :
            if x == y :
                sum1 = sum1 + arr[x][y]

    for x in range(n) :
        for y in range(n) :
            if x + y == n-1:
                sum2 = sum2 + arr[x][y]

    return abs(sum1 - sum2)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)