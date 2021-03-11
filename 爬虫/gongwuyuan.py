import requests
import os
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader, PdfFileWriter, pdf
import pikepdf
import xlsxwriter

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

def down_load(url,dir,name) :
    response = requests.get(url)
    path = 'E:/'+dir+'/'
    pathisExists = os.path.exists(path)
    filepathisExists = os.path.exists(path+name+'.pdf') 
    if pathisExists == False:
        os.mkdir(path)
    if filepathisExists == False :
        with open(path+name+'.pdf', "wb") as code:
            code.write(response.content)

def del_page(path):
    # 读取文件夹下的文件
    # out_path = path +'\out'
    for root,dirs,files in os.walk(path):
        # print(root)     #当前目录路径 
        # print(dirs)     #当前路径下所有子目录 
        # print(files)    #当前路径下所有非目录子文件 
        for file in files:
            # print(file)
            # file1 = os.path.splitext(file)[0]
            # file2 = os.path.splitext(file)[1]
            # print(file1,file2)
            # if os.path.splitext(file)[1] == '.pdf':
            #     filename = os.path.splitext(file)[0]
            #     if 'Unlock' in filename :
            #         filename.replace('Unlock','')
            #     pdfReader = PdfFileReader(open(path+file, 'rb'))
            #     pdfFileWriter = PdfFileWriter()
            #     numPages = pdfReader.getNumPages()
            #     print(numPages)
            #     for i in range(0,numPages):
            #         if i != 1 or i != numPages:
            #             pageObj = pdfReader.getPage(i)
            #             pdfFileWriter.addPage(pageObj)
            #     pdfFileWriter.write(open(path+'out'+filename+'.pdf', 'wb'))   
            if os.path.splitext(file)[1] == '.pdf':
                filepath = path + file
                print(filepath)
                with pikepdf.open(filepath,'wb',allow_overwriting_input=True) as pdf:
                    nums = len(pdf.pages)-2 
                    remove = [0,nums]
                    # print(len(pdf.pages))
                    if 'Unlock' in str(file):
                        file = file.replace('Unlock','')
                        filepath = path + file
                    for index in remove :
                        # print(index)
                        del pdf.pages[index]
                        pdf.save(filepath)

def save_to_excel(city,count,name,link):
    workbook = xlsxwriter.Workbook('e:/'+city+'.xlsx')   #创建一个Excel文件
    worksheet = workbook.add_worksheet('没有下载链接的试卷')  #创建一个sheet
    title = ['试卷名称','打开链接']     #表格title
    worksheet.write_row('A1',title)                 #title 写入Excel
    worksheet.write(count,0,name)
    worksheet.write(count,1,link)


if __name__ == '__main__':
    count = 0
    for page in range(1,13):
        url = 'http://www.chinagwy.org/html/stzx/qt/98_'+str(page)+'.html' 
        # if page == 1:
        response = send_request(url)
        links = get_links(response)
        # print(links)
        names = get_names(response)
        # city为 事业单位 时，下载全部事业单位试卷
        city = '事业单位'

        # 下载真题卷
        for link in links:
            name = names[links.index(link)]
            if city in name:
                response = send_request(link)
                try :
                    download_link = get_download(response)
                    a = down_load(download_link,city,name)
                except :
                    count = count + 1
                    # print(name,link)
                    a = save_to_excel(city,count,name,link)
                    continue
                # download_link = get_download(response)
                # if download_link == None :
                #     count = count + 1
                #     a = save_to_excel(city,count,name,link)
            

    # del_page('E:/解密后/')