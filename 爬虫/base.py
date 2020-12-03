import urllib
import urllib.request as ur
from urllib import parse

url = 'http://passport.baidu.com'
values = {'username':'15251378571','password':'lmm404'}
# values['username'] = '15251378571'
# values['password'] = 'lmm404'

'''
response = urllib.request.urlopen(url)
下面为这个方法的改写，一般使用下面的写法，因为在构建请求时还需要加入好多内容，
通过构建一个 request，服务器响应请求得到应答，这样显得逻辑上清晰明确
'''
# data提交类型不能为str，需要为byte类型
data = parse.urlencode(values).encode('utf-8')
# request = urllib.request.Request(url,data)

# 构建data的第二种方法
# data = parse.urlencode(values)
# geturl = url + '?' + data
# request = urllib.request.Request(geturl)

'''
构建headers
user_agent反爬虫，模拟浏览器请求
referer防盗链服务器会识别 headers 中的 referer 是不是它自己
'''
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer = 'https://passport.baidu.com/v2/?login'
headers = {'user_agent':user_agent,'referer':referer}
request = urllib.request.Request(url,data,headers)

response = ur.urlopen(request)
print(response.read())

# 设置代理，防止访问量过大，被网站踢ip
# enable_proxy = True
# proxy_handler = urllib.request.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib.request.ProxyHandler({})
# if enable_proxy:
#     opener = urllib.request.build_opener(proxy_handler)
# else:
#     opener = urllib.request.build_opener(null_proxy_handler)
# urllib.request.install_opener(opener)