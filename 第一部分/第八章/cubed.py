from decimal import *


def cubed(a):
    try :
        a = Decimal(a)
        a = pow(a,3)
        print(a)
    except (ValueError,InvalidOperation) :
        print('请检查输入内容是否为数字')