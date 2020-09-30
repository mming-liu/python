"""
#第一题
a = "Camus"
for x in a:
    print(x)

#第二题
a = input("请输入：")
b = input("请输入地址：")
a = '"Yesterday I wrote a {}. I sent it to {}"'.format(a,b)
print(a)

#第三题
a = "aldous Huxley was born in 1894.".capitalize()
print(a)

#第四题
a = "Where now? Who now? When now?"
b = a.split("?")
print(b)

# 第五题
list = ["The", "fox", "jumped", "over", "the", "fence", "."]
string = ' '.join(list)
string = string.replace(' .','.') #replace 将末尾的‘ .’替换成'.'
print(string)

#第六题
string = "A screaming comes across the sky."
string = string.replace('s','$')
print(string)

# 第七题
print("Hemingway".index('m'))

#第九题
string = 't'+'h'+'r'+'e'+'e'+' '
string = string * 3
string = string.strip()  #去除首尾空格
print(string)
"""

#第十题
string = "It was bright cold day in April, and the clocks were striking thirteen."
string = string.split(',')
print(string[0])