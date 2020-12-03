import socket
import requests
import socks
from bs4 import BeautifulSoup

url = 'http://maoyan.com/board/4'
headers = {
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cache-Control': 'no-cache',
            # 'Connection': 'keep-alive',
            # 'Host': 'maoyan.com',
            # 'Pragma': 'no-cache',
            # 'Sec-Fetch-Mode': 'navigate',
            # 'Sec-Fetch-Site': 'none',
            # 'Sec-Fetch-User': '?1',
            # 'Upgrade-Insecure-Requests':'1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
# socket.socket = socks.socksocket

response = requests.get(url,headers = headers,verify = False)
# print(response.text)
# ,allow_redirects=False
print(response.request.url)
bsObj = BeautifulSoup(response.text,'lxml')
# film_images = bsObj.select('html body div div div div dl dd a img')
film_images = bsObj.find_all('img',{'class':'board-img'})
for film_image in film_images:
    print(film_image.attrs)
    link = film_image.attrs['data-src'].split('@')
    print(link)
    name = film_image.attrs['alt']
    print(name)