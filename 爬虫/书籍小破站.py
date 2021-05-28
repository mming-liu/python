import os
from time import sleep
from bs4 import BeautifulSoup
import requests
from requests.api import post
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xlsxwriter

url = 'https://www.iamshuaidi.com/753.html'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
links = soup.find_all('li')

names = []
passwords = []
down_links = []
for link in links:
    # print(link.get_text().split(' ')[0],link.get_text().split(' ')[-1])
    # try:
    #     print(link.find('a').get('href'))
    # except :
    #     pass
    try:
        names.append(link.get_text().split(' ')[0])
        passwords.append(link.get_text().split(' ')[-1])
        down_links.append(link.find('a').get('href'))
    except :
        down_links.append(' ')
# print(down_links,len(down_links))

new_names = []
new_passwords = []
new_downlinks = []
for down_link in down_links:
    if 'lanzoui' in down_link or 'baidu' in down_link:
        index = down_links.index(down_link)
        new_names.append(names[index])
        new_passwords.append(passwords[index])
        new_downlinks.append(down_links[index])
print(len(new_names),len(new_passwords),len(new_downlinks))
# print(new_downlinks,len(new_downlinks))


file = 'd:\书籍信息.xlsx'
if os.path.exists(file):
        os.remove(file)
workbook = xlsxwriter.Workbook(file)   #创建一个Excel文件
worksheet = workbook.add_worksheet('所有报名信息')  #创建一个sheet
title = [U'书籍名称',U'链接',U'密码']
worksheet.write_row('A1',title)
row = 1

for i in range(len(new_names)):
    # print(new_names[i],new_passwords[i],new_downlinks[i])
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=chrome_options) 
    # driver = webdriver.Chrome()
    # driver = webdriver.Chrome()
    # time.sleep(10)
    # driver.get(new_downlinks[i])
    # sleep(3)
    # if 'baidu' in new_downlinks[i]:
    #     # driver.find_element_by_id("accessCode").send_keys(new_passwords[i])
    #     # driver.find_element_by_class_name('g-button-right').click()
    #     print(new_names[i],new_downlinks[i],new_passwords[i])
    # else :
    #     print(new_names[i],new_downlinks[i])
    #     # driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="file"]/div[2]/div[5]/iframe'))
    #     # driver.find_element_by_id('go').click()
    book_name = new_names[i]
    book_link = new_downlinks[i]
    book_word = new_passwords[i]
    worksheet.write(row,0,book_name)
    worksheet.write(row,1,book_link)
    worksheet.write(row,2,book_word)
    row = row+1
workbook.close()