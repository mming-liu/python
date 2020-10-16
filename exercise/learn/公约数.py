def hcf(b):
    array_b = []
    count_b = []
    # i+2 是为了避免除以0和1
    for x in b :
        for i in range(x):
            if x % (i+1) == 0 :
                array_b.append(i+1)

    for y in array_b :
        # 计算因数出现的次数等于数组b的长度，可以得出每个元素都有该因数
        if array_b.count(y) == len(b) :
            count_b.append(y)
    # l2 = list(set(l1))   去除数组l1中的重复元素
    # l2.sort(key=l1.index)保持l1的顺序
    # 两条语句合并后，如下
    count_b = sorted(set(count_b),key=count_b.index)
    return count_b

    # 求最大公约数
    # smaller=min(b)
    # for i in reversed(range(1,smaller+1)):
    #     # filter过滤出符合条件的元素，与lambda联合表示把能b数列中整除i的元素过滤出来
    #     if list(filter(lambda j: j%i!=0,b)) == []:
    #         return i


if __name__ == '__main__' :
    # first_multiple_input = input().rstrip().split()
    brr = list(map(int, input().rstrip().split()))
    print(hcf(brr))