import numpy as np

from exercise.learn.多维数组逆时针转动45度 import rotateArr

l = []
u = []
m = [[0 for i in range(3)] for i in range(3)] #创建一个3*3的矩阵
row, col = 0, 1 #初始行列设置01的位置
num = 1
while num <= 9:
    m[row][col] = num #先将01放到第一行中间位置
    num += 1 #每一次循环数字加一
    row -= 1 #下一位数字的行下标
    col += 1 #下一位数字的列下标
    if row < 0 and col >= 3: #判断超出上方行，右方列
        row, col = row + 2, col - 1
    elif row < 0: #判断只有行超出上方行
        row = 3 - 1
    elif col >= 3:#判断只有行超出右方列
        col = 0
    elif m[row][col] != 0:   #判断下一位不为初始值0
        row, col = row + 2, col - 1
#按照列表中存储的数字打印出来

print(m)
n = rotateArr(m)
print(n)

result = [6][6]
for i in range(1,5) :
    result.append(np.rot90(m,i))
    print(result)

for i in range(1,5) :
    result.append(np.rot90(n,i))

# print(result)

