import requests
import os
from bs4 import BeautifulSoup

def send_request(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63'}
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.content.decode('utf-8')
    except Exception as e:
        # print(e)
        return None
    
def get_links(response):
    soup = BeautifulSoup(response, 'lxml')
    list = soup.find(class_='list01').find_all('li')
            # print(list)
    link_list = []
    for item in list:
        links = item.find_all('a')
        for link in links :
            if 'http://www' in str(link) :
                # link_title = link['title']
                link = link.get('href')
                # print(link_title,link)
                link_list.append(link)
    # print(link_list)
    return link_list   

def get_names(response):
    soup = BeautifulSoup(response, 'lxml')
    list = soup.find(class_='list01').find_all('li')
            # print(list)
    name_list = []
    for item in list:
        links = item.find_all('a')
        for link in links :
            if 'http://www' in str(link) :
                link_title = link['title']
                # print(link_title,link)
                name_list.append(link_title)
    # print(link_list)
    return name_list 

def get_download(response):
    soup = BeautifulSoup(response, 'lxml')
    download1 = soup.find('div',id = 'Zoom').find_all('p')
    download2 = soup.find('div',id = 'Zoom').find_all('div')
    for link in download1:
        if '.pdf' in str(link):
            download_link = link.find('a').get('href')
            return download_link
    for link in download2:
        if '.pdf' in str(link):
            download_link = link.find('a').get('href')
            return download_link

def down_load(url,name) :
    # 下载全部事业单位真题卷
    # response = requests.get(url)
    # path = 'E:/事业单位/'
    # pathisExists = os.path.exists(path)
    # filepathisExists = os.path.exists(path+name+'.pdf') 
    # if pathisExists == False:
    #     os.mkdir(path)
    # if filepathisExists == False :
    #     with open(path+name+'.pdf', "wb") as code:
    #         code.write(response.content)

    # 下载江苏事业单位真题卷
    response = requests.get(url)
    path = 'E:/江苏/'
    pathisExists = os.path.exists(path)
    filepathisExists = os.path.exists(path+name+'.pdf') 
    if pathisExists == False:
        os.mkdir(path)
    if filepathisExists == False :
        with open(path+name+'.pdf', "wb") as code:
            code.write(response.content)

if __name__ == '__main__':
    for page in range(1,13):
        url = 'http://www.chinagwy.org/html/stzx/qt/98_'+str(page)+'.html' 
        # if page == 1:
        response = send_request(url)
        links = get_links(response)
        names = get_names(response)

        # 下载所有的事业单位真题卷
        # for link in links:
            # response = send_request(link)
            # download_link = get_download(response)
            # # print(download_link)
            # # response = send_request(download_link)
            # index = links.index(link)
            # # print(index)
            # print(names[index])
            # a = down_load(download_link,names[index])
            # # print('下载成功')

        # 下载江苏的真题卷
        for link in links:
            name = names[links.index(link)]
            if '江苏' in name:
                response = send_request(link)
                download_link = get_download(response)
                a = down_load(download_link,name)