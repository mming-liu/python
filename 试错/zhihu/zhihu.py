import warnings
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

warnings.filterwarnings("ignore")   #不提示警示信息
url = 'https://www.zhihu.com/people/brother_cat/zvideos'
# driver = webdriver.Chrome()   #需要调用浏览器
# 创建chrome参数对象
opt = webdriver.ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
opt.set_headless()
# 创建chrome无界面对象
driver = webdriver.Chrome(options=opt)
try:
    driver.get(url)
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'//*[@id="Profile-zvideos"]/div[2]/div[21]')))

    element = driver.find_element_by_xpath('//*[@id="Profile-zvideos"]/div[2]/div[21]')
    if element.is_displayed() == True:
        pages = element
    else:
        driver.refresh()
    # print(pages.text)
    pages = str(pages.text).split('...')[1].split('下一页')[0]
    # print(pages)

    links = []
    titles = []
    for i in range(1,int(pages)+1):
        driver.get('http://www.zhihu.com/people/brother_cat/zvideos?page='+str(i))
        # WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'//*[@id="Profile-zvideos"]/div[2]/div[21]/button['+str((i+1))+']')))
        response_str = driver.page_source
        # print(response_str)

        bsObj = BeautifulSoup(response_str,'lxml')
        video_ifm = bsObj.select('h2 a')
        # print(video_ifm)

        for a in video_ifm:
            link = str(a)
            link = link.split('href="')[1].split('" rel')[0]
            title = a.text
            links.append(link)
            titles.append(title)

    # print(links)
    # print(titles)
    # print(len(links),len(titles))

    failed_video = []
    for m in range(178, len(links)) :
        for n in range(178, len(titles)):
            if m == n :
                try:
                    driver.get(links[m])
                    response_video = driver.page_source
                    # print(response_video)
                    response_video = BeautifulSoup(response_video,'lxml')
                    src_link = str(response_video.select('iframe')).split('src="')[1].split('"')[0]
                    src_link = src_link.replace('https://www.zhihu.com/video/','https://lens.zhihu.com/api/v4/videos/')
                    # print(src_link)

                    driver.get(src_link)
                    response_link = driver.page_source
                    # print(response_link)
                    response_link = str(response_link).split('"play_url": "')[1].split('", "height"')[0].split('amp;')
                    # print(response_link)
                    new_link = ''
                    for str_link in range(len(response_link)):
                        # print(response_link[m])
                        new_link = new_link+ response_link[str_link]
                    # print(new_link)

                    path = 'D://批量下载视频/'
                    res = requests.get(new_link,verify=False,allow_redirects=False)
                    with open(path+str(titles[n])+'.mp4', 'wb') as f:
                        print('这是第'+str(m+1)+'个视频',str(titles[n]))
                        f.write(res.content)
                except Exception as e:
                    print(e)
                    failed_video.append(str(titles[n]))
                    break
    print(failed_video)
except :
    driver.quit()
driver.quit()
