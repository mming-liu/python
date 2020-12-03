import http.cookiejar as cookielib
import urllib

def cookies(url):
    """保存cookies到变量
    """
    #声明一个CookieJar对象实例来保存cookie
    cookie = cookielib.CookieJar()
    # HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib.request.HTTPCookieProcessor(cookie)
    #通过handler来构建opener
    opener = urllib.request.build_opener(handler)
    #此处的open方法同urlopen方法，也可以传入request
    response = opener.open(url)
    # for item in cookie:
    #     print ('Name = '+item.name)
    #     print ('Value = '+item.value)

def save_cookies_Moz(url):
    """保存cookies到文件 —— Netscape格式
    """
    filename = 'cookies_Moz.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)       # 这里必须将参数置为True，否则写入文件失败

def save_cookies_LWP(url):
    """保存cookies到文件 —— LWP格式
    """
    filename = 'cookies_LWP.txt'
    cookie = cookielib.LWPCookieJar(filename)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)       # 这里必须将参数置为True，否则写入文件失败

def read_cookies_LWP(url):
    """
    读取保存的cookies文件
    """
    filename = 'cookies_LWP.txt'
    cookie = cookielib.LWPCookieJar()
    cookie.load(filename,ignore_discard=True, ignore_expires=True)
    print(cookie)
    request = urllib.request.Request(url)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)

if __name__ == '__main__' :
    url = 'https://www.zhihu.com'
    cookies(url)
    save_cookies_LWP(url)
    read_cookies_LWP(url)