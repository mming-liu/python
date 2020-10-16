def lcm(a):
    greater=max(a)
    while True:
        # 从数列的最大值开始，计算能够整除列表元素的数
        if list(filter(lambda i: greater%i!=0,a)) == []:
            return greater
        greater+=1

    return x


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(lcm(arr))
