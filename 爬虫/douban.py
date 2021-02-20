import requests
import xlsxwriter
from bs4 import BeautifulSoup

class douban():

    def main(self,page):
        self.url = 'https://movie.douban.com/top250?start='+str(page * 25)+'&filter='
        self.heards = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63'}
        response = self.send_request()
        self.soup = BeautifulSoup(response, 'lxml')
        do_soup = self.do_soup()
        self.save_to_excel()

    def send_request(self):
        try:
            response = requests.get(self.url,headers = self.heards)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(e)
            return None

    def do_soup(self):
        list = self.soup.find(class_='grid_view').find_all('li')
        for item in list:
            self.item_name = item.find(class_='title').string
            self.item_img = item.find('a').find('img').get('src')
            self.item_index = item.find(class_='').string
            self.item_score = item.find(class_='rating_num').string
            self.item_author = item.find('p').text
            self.item_intr = item.find(class_='inq').string
            return self.item_name,self.item_img,self.item_index,self.item_score,self.item_author,self.item_intr

    def save_to_excel(self):
        workbook = xlsxwriter.Workbook('e:\豆瓣.xlsx')   #创建一个Excel文件
        worksheet = workbook.add_worksheet('爬取电影')  #创建一个sheet
        # title = [self.item_index ,self.item_name,self.item_score,self.item_intr]     #表格title
        title = [U'序号',U'电影名称',U'评分',U'别名']
        worksheet.write_row('A1',title)                    #title 写入Excel
        for i in range(1,25):
            worksheet.write(i,0,self.item_index)
            worksheet.write(i,1,self.item_name)
            worksheet.write(i,2,self.item_score)
            worksheet.write(i,3,self.item_intr)
            i+=1
        workbook.close()


if __name__ == '__main__' :
    a = douban()
    for i in range(0,9):
        a.main(i)

    # soup = a.main(0)
    # list = soup.find(class_='grid_view').find_all('li')
    # # print(list)
    # for item in list:
    #     item_name = item.find(class_='title').string
    #     item_img = item.find('a').find('img').get('src')
    #     item_index = item.find(class_='').string
    #     item_score = item.find(class_='rating_num').string
    #     item_author = item.find('p').text
    #     item_intr = item.find(class_='inq').string
    #     print('爬取电影：' + item_index + ' | ' + item_name  +' | ' + item_score  +' | ' + item_intr )


# with open('E:\\douban.html','a',encoding='utf-8') as f:
    #     f.write(b.text)
    # print('write success')
