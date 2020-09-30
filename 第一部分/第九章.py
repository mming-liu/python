import csv
import os

# # 打印文本文档
# path = os.path.join(r"C:\Users\ccc\Desktop\国寿\国寿.txt")
# # path = os.path.join("C:\\Users\\ccc\\Desktop\\国寿\\国寿.txt")
# with open(path,'r',encoding='UTF-8') as f:
#     print(f.read())
#
# # f = open(path,'r',encoding='UTF-8')
# # print(f.read())
# # f.close()
#
# path = os.path.join(r'C:\Users\ccc\Desktop\kpi\KPI接口数据与数据库比对.csv')
# with open(path,'r',encoding='UTF-8') as f:
#     print(f.read())

# 第二题
# path = os.path.join(r'C:\Users\ccc\Desktop\1.txt')
# with open(path,'w',encoding='UTF-8') as f:
#     f.write(input('输入一段话:'))
# with open(path,'r',encoding='UTF-8') as f:
#     print(f.read())

path = os.path.join(r'C:\Users\ccc\Desktop\1.csv')
with open(path,'w',newline = '') as f:
    w = csv.writer(f,delimiter=',')
    w.writerow(["Top Gun", "Risky Business","Minority Report"])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Training Day", "Man on Fire", "Flight"])
with open(path,'r',encoding='UTF-8') as f:
    r = csv.reader(f,delimiter=',')
    for row in r :
#        print(row)
        print(','.join(row))