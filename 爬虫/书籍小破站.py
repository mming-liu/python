import json
import os
import re
from time import sleep
import time
from bs4 import BeautifulSoup
import requests
from requests.api import post
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xlsxwriter

# url = 'https://www.iamshuaidi.com/753.html'
# response = requests.get(url)
# soup = BeautifulSoup(response.text,'lxml')
# links = soup.find_all('li')

# names = []
# passwords = []
# down_links = []
# for link in links:
#     # print(link.get_text().split(' ')[0],link.get_text().split(' ')[-1])
#     # try:
#     #     print(link.find('a').get('href'))
#     # except :
#     #     pass
#     try:
#         names.append(link.get_text().split(' ')[0])
#         passwords.append(link.get_text().split(' ')[-1])
#         down_links.append(link.find('a').get('href'))
#     except :
#         down_links.append(' ')
# # print(down_links,len(down_links))

# new_names = []
# new_passwords = []
# new_downlinks = []
# for down_link in down_links:
#     if 'lanzoui' in down_link or 'baidu' in down_link:
#         index = down_links.index(down_link)
#         new_names.append(names[index])
#         new_passwords.append(passwords[index])
#         new_downlinks.append(down_links[index])
# print(len(new_names),len(new_passwords),len(new_downlinks))
# print(new_downlinks,len(new_downlinks))


# file = 'd:\书籍信息.xlsx'
# if os.path.exists(file):
#         os.remove(file)
# workbook = xlsxwriter.Workbook(file)   #创建一个Excel文件
# worksheet = workbook.add_worksheet('书籍信息')  #创建一个sheet
# title = [U'书籍名称',U'链接',U'密码']
# worksheet.write_row('A1',title)
# row = 1

# for i in range(len(new_names)):
#     book_name = new_names[i]
#     book_link = new_downlinks[i]
#     book_word = new_passwords[i]
#     worksheet.write(row,0,book_name)
#     worksheet.write(row,1,book_link)
#     worksheet.write(row,2,book_word)
#     row = row+1
# workbook.close()

# for i in range(len(new_names)):
#     print(new_names[i],new_passwords[i],new_downlinks[i])
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     driver = webdriver.Chrome(chrome_options=chrome_options) 
#     # driver = webdriver.Chrome()
#     time.sleep(10)
#     driver.get(new_downlinks[i])
#     sleep(3)
#     if 'baidu' in new_downlinks[i]:
#         # driver.find_element_by_id("accessCode").send_keys(new_passwords[i])
#         # driver.find_element_by_class_name('g-button-right').click()
#         print(new_names[i],new_downlinks[i],new_passwords[i])
#     else :
#         print(new_names[i],new_downlinks[i])
#         # driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="file"]/div[2]/div[5]/iframe'))
#         # driver.find_element_by_id('go').click()


url = 'https://wws.lanzoui.com/iQUI9kdrgqh'
 
#header头，注意那个referer必须要与上面文件分享地址url相同
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.3',
    'referer': url
}
 
# 获取分享页面html文件
res = requests.get(url,headers=headers)
# print(res.text)
 
# 引入BeautifulSoup库对html进行处理，获取iframe中的出现的js文件
soup = BeautifulSoup(res.text,'html.parser')
url2 = url+soup.find('iframe').get('src')
print(url2)
res2 = requests.get(url2,headers=headers)

# print(res2.text)


 
# 正则提取请求三个参数
a = re.findall(r'var a = \'([\w]+?)\';',res2.text)
print(a)
params = re.findall(r'var [\w]{6} = \'([\w]+?)\';',res2.text)
print(params)
 
# 请求下载地址
url3 = 'https://www.lanzous.com/ajaxm.php'
data = {
    'action':'down_process',
    'file_id':params[0],
    't':params[1],
    'k':params[2],
}
# print(data)
# res3 = requests.post(url3,headers=headers,data=data)
# res3 = json.loads(res3.content)
 
# # 请求最终重定向地址
# url4 = res3['dom']+'/file/'+res3['url']
# headers2 = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
#     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# }
# res4 = requests.head(url4, headers=headers2)
# print (res4.headers['Location'])
