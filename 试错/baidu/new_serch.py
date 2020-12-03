import urllib

import requests
from bs4 import BeautifulSoup
from lxml import etree

class link_action():
    def __init__(self,table,path1,path2,element,str1,str2):
        self.table = table
        self.path1 = path1
        self.path2 = path2
        self.element = element
        self.str1 = str1
        self.str2 = str2

    def links(self,table,request_url):
        session = requests.session()
        self.response = session.get(request_url,allow_redirects=False)
        print(request_url)
        bsObj = BeautifulSoup(self.response.text,'lxml')
        print(bsObj.text)
        self.h3 = bsObj.select(table)
        return self.h3

    def actions(self,path1,path2,element):
        tree = etree.HTML(self.response.content)
        links = []
        for xpath in self.xpaths:
            for link in tree.xpath(xpath):
                link = str(etree.tostring(link))
                link = link[link.rfind(path1):link.rfind(path2)].replace(path1,'')
                if element in link :
                    links.append(link)
        return links

    def xpath(self,str1,str2):
        self.xpaths = []
        for i in range(len(self.h3)):
            xpath = str1+str(i+1)+str2
            self.xpaths.append(xpath)
        return self.xpaths

if __name__ == '__main__':
    get_data={'wd':'美女'}
    get_data_encode=urllib.parse.urlencode(get_data)
    request_url='http://www.baidu.com/s'
    request_url+='?'+get_data_encode
    link_action = link_action('h3','href="','" ','www.baidu.com','//*[@id="','"]/h3/a')
    # result = link_action('h3','href="','" ','www.baidu.com','//*[@id="','"]/h3/a')
    table = link_action.links('h3',request_url)
    xpath = link_action.xpath('//*[@id="','"]/h3/a')
    links = link_action.actions('href="','" ','www.baidu.com')
    # print(links)
    for link in links:
        # print(link)
        image_link = link_action.__init__('body div div div div ul li','data-objurl="','" ','http:','//*[@id="imgid"]/div/ul/li[',']')
        image_table = link_action.links('body div div div div ul li',link)
        # print(image_table)
        # image_xpath = link_action.xpath('//*[@id="imgid"]/div/ul/li[',']')
        # print(image_xpath)
        # image_links = link_action.actions('data-objurl="','" ','http:')
        # print(image_links)