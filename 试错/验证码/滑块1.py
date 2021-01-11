import time
from collections import Counter

from PIL import Image
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class maoyan_slide():
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.set_headless()
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get('https://passport.maoyan.com/verify?redirectURL=http%3A%2F%2Fmaoyan.com%2Fboard%2F4&requestCode=9261b9c5d90c9cedcfe3c5924ff364e8yszvz')
        time.sleep(2)

    def get_picture(self):
        #等到iframe加载出来再操作
        ifarme = '//*[@id="tcaptcha_iframe"]'
        WebDriverWait(self.driver,60).until(EC.presence_of_element_located((By.XPATH,ifarme)))
        #先要把光标切换到iframe才能找到图片
        self.driver.switch_to.frame('tcaptcha_iframe')
        #背景图片的xpath，带缺口的
        picture_back = '//*[@id="slideBg"]'
        self.driver.find_element_by_xpath(picture_back)
        #滑块的xpath
        picture_slide = '//*[@id="slideBlock"]'
        self.driver.find_element_by_xpath(picture_slide)

    def shape(self, w, h, image):  # 二值化，将所有的点位，全部换成0或255
        tem = 0
        for x in range(w):
            for y in range(h):
                tem += image.getpixel((x, y))
        pixel_ave = tem / w / h * 0.7
        for x in range(w):
            for y in range(h):
                p = image.getpixel((x, y))
                if p < pixel_ave:
                    image.putpixel((x, y), 0)
                else:
                    image.putpixel((x, y), 255)
        return image

    def reducenoise(self, image):#降噪处理
        w, h = image.size
        for x in range(0, 40):  # 处理最左边
            for y in range(h):
                image2 = image.putpixel((x, y), 255)
        return image

    def make_picture(self):  # 处理图片，灰度化与二值化、降噪
        im = Image.open('slice.png')
        im2 = im.convert("L")
        w, h = im2.size
        im3 = self.shape(w, h, im2)
        im4 = self.reducenoise(im3)
        return im3

    def get_juli(self, image):  # 计算距离
        w, h = image.size
        ls = []
        for i in range(31, w - 31):#图片最左边放置滑块，缺口坐标x不可能小于31
            for j in range(10, h):
                if image.getpixel((i, j)) < 100:
                    count = 0
                    for k in range(i, i + 31):
                        if image.getpixel((k, j)) < 100:
                            count += 1
                        else:
                            break
                    if count > 27: ls.append(i)
        return Counter(ls).most_common(1)[0][0]

    def get_track(self, distance):  # 设计拖动轨迹
        ls = [1]
        while 1:
            i = ls[-1] * 2
            ls.append(i)
            if sum(ls) > distance * 0.7:
                break

        ls.append(int(distance - sum(ls)))
        return ls

    def drog_btn(self, track):  # 拖动滑块
        #定位滑块
        ele = self.driver.find_element_by_xpath('.//div[@class="JDJRV-slide-inner JDJRV-slide-btn"]')
        #设计拖动动作链（点击且不放）
        ActionChains(self.driver).click_and_hold(ele).perform()
        #根据设计的轨迹，实现滑块拖动
        for i in track:
            ActionChains(self.driver).move_by_offset(i, 0).perform()
        #睡眠0.25秒，伪装成人的判断过程
        time.sleep(0.25)
        #释放滑块，类似于松开鼠标
        ActionChains(self.driver).release().perform()
        time.sleep(2)

    def check(self):#再次尝试
        self.get_picture()
        image = self.make_picture()
        distance = self.get_juli(image)
        track = self.get_track(distance)
        self.drog_btn(track)



if __name__ == '__main__':
    # url = 'https://blog.csdn.net/KiM_LYJ/article/details/105984755'
    login = maoyan_slide()
    login.get_picture()
    image = login.make_picture()
    distance = login.get_juli(image)
    track = login.get_track(distance)
    login.drog_btn(track)
    time_int = 0
    while time_int < 5:
        input("是否需要再次尝试")
        login.driver.refresh()
        login.check()
        time_int += 1