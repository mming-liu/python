from appium import webdriver
import time

desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1'
desired_caps['deviceName'] = '192.168.145.101:5555'
desired_caps['appPackage'] = 'com.ss.android.article.lite'
desired_caps['appActivity'] = 'com.ss.android.article.lite.activity.SplashActivity'
desired_caps['noReset'] = 'True'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
