import requests
from bs4 import BeautifulSoup

url = 'http://www.zhihu.com/billboard'

pre = {'User-Agent':'Mozilla/5.0'}
res = requests.get(url,headers = pre)
rep = res.text
print(rep)
print('---------------------------------------')
soup = BeautifulSoup(rep,"html.parser")
print(soup)