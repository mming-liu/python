import time

from PIL import Image
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

if __name__ == '__main__':
