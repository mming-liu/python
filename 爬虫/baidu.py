'''
moonshad。js是经过混淆码处理的，暂时没办法
'''


# import time
# import urllib
# from _md5 import md5
# from binascii import b2a_hex
# from urllib import parse
# import urllib.request as ur
#
# import execjs
# import requests
# from cryptography.hazmat.primitives.ciphers.algorithms import AES
#
# url = 'http://www.baidu.com'
# url_pass = 'http://passport.baidu.com/v2/api/'
# # values = {'username':'15251378571','password':'lmm404'}
# # data = parse.urlencode(values).encode('utf-8')
# header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# # response = requests.get(url=url,headers = header,verify=False)
#
# def _get_runntime():
#     """
#     :param path: 加密js的路径,注意js中不要使用中文！估计是pyexecjs处理中文还有一些问题
#     :return: 编译后的js环境，不清楚pyexecjs这个库的用法的请在github上查看相关文档
#     """
#     phantom = execjs.get()  # 这里必须为phantomjs设置环境变量，否则可以写phantomjs的具体路径
#     with open('baidulogin.js', 'r') as f:
#         source = f.read()
#     return phantom.compile(source)
#
# def get_gid():
#     return _get_runntime().call('getGid')
#
# def get_callback():
#     return _get_runntime().call('getCallback')
#
# def _get_curtime():
#     return int(time.time()*1000)
#
# def r(x):
#     o = md5("&".join([f"{n}={x[n]}" for n in sorted([t for t in x])]))
#     h = {"0":"s","1":"t","2":"r","3":"h","4":"i","5":"j","6":"k","7":"l","8":"m","9":"n","a":"3","b":"4","c":"5","d":"9","e":"8","f":"7","g":"1","h":"2","i":"6","j":"0","k":"a","l":"b","m":"c","n":"d","o":"e","p":"f","q":"g","r":"z","s":"y","t":"x","u":"w","v":"v","w":"u","x":"o","y":"p","z":"q"}
#     a = ""
#     s = ["1", "9", "2", "0", "1", "0", "8", "0"]
#     for n in s:
#         a += h[n]
#     return f(o, a)
#
# def f(x, c):
#     t, r, n = "", list(x), list(c)
#     if len(r) >= len(n):
#         for _ in range(len(n)):
#             t += r[_] + n[_]
#         t += x[_+1:]
#     else:
#         for _ in range(len(r)):
#             t += r[_] + n[_]
#         t += c[_+1:]
#     return t
#
# def add_to_16(text):
#     if len(text.encode('utf-8'))%16:
#         add = 16 - len(text.encode('utf-8')) % 16
#     else:
#         add = 0
#     text = text + ("\0"*add)
#     return text.encode('utf-8')
#
# def encrypt(text):
#     key = "_".encode('utf-8')
#     mode = AES.MODE_ECB
#     text = add_to_16(text)
#     cryptos = AES.new(key, mode)
#     cipher_text = cryptos.encrypt(text)
#     return b2a_hex(cipher_text)
#
# def get_url():
#     values = {'getapi':'',
#               'token':'',
#               'tpl':'mn',
#               'subpro':'',
#               'apiver':'v3',
#               'tt':_get_curtime(),
#               'class':'login',
#               'gid':get_gid(),
#               'loginversion':'v4',
#               'logintype':'dialogLogin',
#               'traceid':'',
#               'time':int(time.time()),
#               'alg':'v3',
#               'sig':'M3ZjUEd6S0ZnSElNS2NGNFNSUklXWVpaNnVlSURncThuWmM0dDhFSWhUcGFaNVlPcm1JQk1rdUkvcmRsbnh3cQ==',
#               'elapsed':'54',
#               'shaOne':'00e6f78fc4c91c06a24ae5fc7941742e4b86564d',
#               'callback':get_callback()
#               }
#     data = parse.urlencode(values)
#     return url_pass +'?'+ data
#
# if __name__ == '__main__' :
#     session = requests.Request()
#     request = urllib.request.Request(get_url())
#     response = ur.urlopen(request)
#     print(response.url)