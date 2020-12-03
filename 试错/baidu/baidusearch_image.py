import os
import urllib.parse
import requests
from bs4 import BeautifulSoup
from lxml import etree
from requests import ReadTimeout
from selenium import webdriver

get_data={'wd':input('请输入想要搜索的图片：')}
get_data_encode=urllib.parse.urlencode(get_data)
request_url='http://www.baidu.com/s'
request_url+='?'+get_data_encode
session = requests.session()
response = session.get(request_url)
page_sourse=response.text.encode('utf-8')
with open('baidu.html','wb') as f:
    f.write(page_sourse)
    f.close()
bsObj = BeautifulSoup(response.text,'lxml')
h3 = bsObj.select('h3')
tree = etree.HTML(response.content)
# print(etree.tostring(tree).decode('utf-8'))
links = []
for i in range(len(h3)):
    for link in tree.xpath('//*[@id="'+str(i+1)+'"]/h3/a'):
        link = str(etree.tostring(link))
        link = link[link.rfind('href="'):link.rfind('" ')].replace('href="','')
        if 'www.baidu.com' in link :
            links.append(link)

for link in links:
    response_image = session.get(link,verify=False,allow_redirects=False)
    loaction = response_image.headers['Location']
    print(loaction)

    browser = webdriver.PhantomJS()
    browser.get(loaction)
    image_link = BeautifulSoup(browser.page_source,'lxml')
    # print(image_link)
    img_links = browser.find_elements_by_xpath('//*[@id="imgid"]/div/ul/li')
    # print(browser.find_element_by_xpath('//*[@id="imgid"]/div/ul/li[1]').text)
    for img_link in img_links :
        path = 'D:/批量下载图片/'
        if not os.path.exists(path):
            os.mkdir(path)
        img_link = img_link.get_attribute('data-objurl')
        try :
            res = requests.get(img_link,timeout=3,verify=False,allow_redirects=False)
            with open(path+str(i)+".jpg", 'wb') as f:
                f.write(res.content)
            i = i+1
        except ReadTimeout:
            continue
browser.quit()