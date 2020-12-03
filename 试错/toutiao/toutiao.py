import time
from urllib import parse
import requests

header = {
    'origin':'https://learning.snssdk.com',
    'user-agent':'Mozilla/5.0 (Linux; Android 10; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.156 Mobile Safari/537.36 JsSdk/2 NewsArticle/7.7.1 NetType/wifi (NewsLite 7.7.1) TTWebView/0751130011014',
    'accept':'*/*',
    'referer':'https://learning.snssdk.com/feoffline/purchasedcontent/my_column.html',
    'accept-encoding':'gzip, deflate',
    'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie':'gfsitesid=OWFiNDIwZDFlM3wxNjA2MjA5MTI3ODN8fDMwMDM0ODc4NTk3NzMwOTkHBwcHBwcH',
    # 'cookie':'uid_tt=7922cc00a3063f7c4ae8e133e856f169',
    # 'cookie':'uid_tt_ss=7922cc00a3063f7c4ae8e133e856f169',
    # 'cookie':'sid_tt=9ab420d1e3fca4d0f7e9313b02b77a14',
    # 'cookie':'sessionid=9ab420d1e3fca4d0f7e9313b02b77a14',
    # 'cookie':'sessionid_ss=9ab420d1e3fca4d0f7e9313b02b77a14',
    # 'cookie':'PIXIEL_RATIO=3',
    # 'cookie':'UM_distinctid=173eb710c74220-00c3d291a240e4-7d664551-261150-173eb710c7520c',
    # 'cookie':'learning_shelf_visited=1',
    # 'cookie':'FRM=new',
    # 'cookie':'d_ticket=e6cfff39fbdc0f616889a68a256156857df37',
    # 'cookie':'odin_tt=cf1e191f76427e74c095d714c3e400660cc822d9156763bdf03188322f2d9e88484a3e3e03ec0e02d4846a31c416231792689009cfbe5aa85f50f6a0a3d27932',
    # 'cookie':'passport_csrf_token=249e933569ab478e302484942bcd3f1a',
    # 'cookie':'SLARDAR_WEB_ID=70779461-a527-4cea-adef-6af839cc98f2',
    # 'cookie':'ssr_tz=Asia/Shanghai',
    # 'cookie':'ssr_sbh__=34',
    # 'cookie':'sid_guard=9ab420d1e3fca4d0f7e9313b02b77a14%7C1605240935%7C5182308%7CTue%2C+12-Jan-2021+03%3A47%3A23+GMT',
    # 'cookie':'WIN_WH=360_684',
    # 'cookie':'gftoken=OWFiNDIwZDFlM3wxNjA2MjA5MTI3ODN8fDAGBgYGBgY',
    # 'cookie':'install_id=1829226113413805',
    # 'cookie':'ttreq=1$7eac7d7882e7fb560b02e485c50acf5cad194196',
    # 'cookie':'MONITOR_WEB_ID=e2b77f89-fb93-48e1-9bbe-079411c14a21'
}

query_string = {
    'ev_type':'ajax',
    'ax_status':'200',
    'ax_type':'get',
    'ax_request_header':'',
    'ax_duration':'344',
    'ax_size':'6174',
    'ax_response_header':'content-type: application/json; charset=utf-8',
    'ax_protocol':'https',
    'ax_domain':'i.snssdk.com',
    'ax_path':'/slardar/sdk_setting',
    'ax_url':'https://i.snssdk.com/slardar/sdk_setting',
    'version':'2.0.24',
    'hostname':'learning.snssdk.com',
    'protocol':'https',
    'url':'https://learning.snssdk.com/feoffline/purchasedcontent/my_column.html',
    'slardar_session_id':'4673ff84-e0e2-4c8e-8fb5-aead6f09e794',
    'sample_rate':'1',
    'pid':'my_column',
    'report_domain':'i.snssdk.com',
    'bid':'toutiao_purchased_content',
    'context':'{"app_name":"news_article"}',
    'slardar_web_id':'c96fb5bf-4e8a-4e24-89bb-cbd43bd9b54c',
    'timestamp':int(time.time()*1000)
}


url = 'https://learning.snssdk.com/feoffline/purchasedcontent/my_column.html'
data = parse.urlencode(query_string)
url = url+'?'+data
print(url)
response = requests.get(url,headers = header, verify = False)
print(response.text)