def rotateArr(arr):
    new_arr = []
    lens = len(arr)
    # 打印二维数组右上半部分
    i = lens - 1
    while i > 0:
        row = 0
        col = i
        while col < lens:
            new_arr.append(arr[row][col])
            row += 1
            col += 1
        i -= 1

    # 打印二维数组左下半部分
    i = 0
    while i < lens:
        row = i
        col = 0
        while row < lens:
            new_arr.append(arr[row][col])
            row += 1
            col += 1
        i += 1

    for i in range(3) :
        for j in range(3) :
            arr[i][j] = new_arr[i+j]

    return arr
    # return new_arr

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotateArr(arr))