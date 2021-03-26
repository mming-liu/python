import json
import jsonpath
from jsonpath_ng import parse
# https://blog.csdn.net/nd211314555/article/details/88426529 jsonpath的基本操作

path = 'C:/Users/ccc/Desktop/APD/5.0报文/处理损失项目.txt'
with open(path,'r',encoding='utf-8') as f:
    data = f.read()
    data = eval(data)
    # print(data)

laborValue1 = jsonpath.jsonpath(data,expr='$.claimLabors[*].laborFeeAfterDiscount')
laborValue2 = jsonpath.jsonpath(data,expr='$.claimLabors[*].operationType')

partQuantity = jsonpath.jsonpath(data,expr='$.claimParts[*].partQuantity')
unitPrice = jsonpath.jsonpath(data,expr='$.claimParts[*].unitPrice')

print(partQuantity,unitPrice)
lenth = len(partQuantity)
print(lenth)
if lenth >= 1 :
    for i in range(1,lenth+1):
        print(i, i % 2)
        if i % 2== 1:
            path = '$.claimParts['+str(i-1)+'].partQuantity'
            part_quantity = partQuantity[i-1]+2
            jsonpath_expr  = parse(path)
            jsonpath_expr.find(data)
            updated_json = jsonpath_expr.update(data, part_quantity)
        else :
            path = '$.claimParts['+str(i-1)+'].unitPrice'
            unit_Price = unitPrice[i-1]+1000
            jsonpath_expr  = parse(path)
            jsonpath_expr.find(data)
            updated_json = jsonpath_expr.update(data, unit_Price)

for m in laborValue2:
    if m == '03':
        # print(laborValue2.index(m))
        path = '$.claimLabors['+str(laborValue2.index(m))+'].laborFee'
        # print(path)
        paint_fee = laborValue1[laborValue2.index(m)]+1000
        jsonpath_expr  = parse(path)
        jsonpath_expr.find(data)
        updated_json = jsonpath_expr.update(data, paint_fee)
        # list的值重复时，只能去到第一个index，所以该list中的值，才能取到符合条件的下一个值
        laborValue2[laborValue2.index(m)] = '05'
    elif m == '02' or m == '04':
        path = '$.claimLabors['+str(laborValue2.index(m))+'].laborFeeAfterDiscount'
        # print(path)
        labor_fee = laborValue1[laborValue2.index(m)]+1000
        jsonpath_expr  = parse(path)
        jsonpath_expr.find(data)
        updated_json = jsonpath_expr.update(data, labor_fee)
        # list的值重复时，只能去到第一个index，所以该list中的值，才能取到符合条件的下一个值
        laborValue2[laborValue2.index(m)] = '05'

print(data)