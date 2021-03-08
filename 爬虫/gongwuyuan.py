import requests
from requests.models import Response
import xlsxwriter
from bs4 import BeautifulSoup

class shiye():

        def main(self,page):
            self.url = 'http://www.chinagwy.org/html/stzx/qt/98_'+str(page)+'.html'
            self.heards = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63'}
            response = self.send_request()
            self.soup = BeautifulSoup(response, 'lxml')
            links = self.do_soup()
            # print(links)
            return links
        
        def send_request(self):
            try:
                response = requests.get(self.url,headers = self.heards)
                if response.status_code == 200:
                    return response.content.decode('utf-8')
            except Exception as e:
                print(e)
                return None
        
        def do_soup(self):
            list = self.soup.find(class_='list01').find_all('li')
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

if __name__ == '__main__':
    a = shiye()
    open_links = []
    for i in range(1,13):
        open_links.append(a.main(i))
    # print(open_links)

    for i in open_links:
        for j in i:
            response = requests.get(j)
            response = response.content.decode('utf-8')
            soup = BeautifulSoup(response, 'lxml')
            download = soup.find('div',id = 'Zoom').find_all('p')
            name = soup.find('div',id = 'Zoom').find('p').string
            print(name)
            # print(download)
            # for p in download :
            #     # name = p[0]
            #     # link = p[1]
            #     # print(name,link)
            #     if '.pdf' in str(p):
            #         download_link = p.find('a').get('href')
            #         print(download_link)
            #     #     down_response = requests.get(download_link)
            #     # down_response = requests.get(link)
            #     # with open('E:\\'+name+'.pdf', "wb") as code:
            #     #     code.write(down_response.content)
            

    # soup = a.main(1)
    # list = soup.find(class_='list01').find_all('li')
    # print(list)
    # for item in list:
    #     links = item.find_all('a')
    #     for link in links :
    #         if 'http://www' in str(link) :
    #             link_title = link['title']
    #             link = link.get('href')
    #             print(link_title,link)

                