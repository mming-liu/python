import time

import requests

from 试错.baidu.save_cookies import save_cookies_LWP, read_cookies_LWP

# url = 'http://www.baidu.com'
# hearders = {
#     'Host': 'www.baidu.com',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Connection': 'keep-alive'
# }
#
# response = requests.get(url,headers=hearders,verify=False)
# save_cookies_LWP(url)
#
# tt = str(int(time.time()*1000))
# url_token = 'http://wappass.baidu.com/static/waplib/moonshad.js?tt='+tt
# print(url_token)
# hearders.update(dict( Referer='http://www.baidu.com/',Host = 'wappass.baidu.com',Cookie = read_cookies_LWP(url)))
# response1 = requests.get(url,headers=hearders,stream=True,verify=False)
# print(response1.text)

from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get('https://www.baidu.com')
print(browser.current_url)