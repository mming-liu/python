'''
# 第一题和第三题
list = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for x in list:
    print(x)
    print(list.index(x))

#第二题
for x in range(25,51):
    print(x)

#第四题
list = [1,3,5,7,9]
while True :
    print("输入‘Q’可以退出循环")
    try :
        a = input('请输入一个数字：')
        if a == 'q' or a== 'Q':
            break
        for x in list:
            if x == float(a):  #用int，输入小数会走到except
                print("输入正确")
                break
        else :
            print("输入错误")
    except ValueError :
        print('请检查是否输入了数字或者Q')
'''

#第五题
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
time = []
for x in list1 :
    for y in list2 :
        time.append(x * y)
        time.append(x + y)
print(time)
