# -*- coding = utf-8 -*-
from random import choice
# selenium显式等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from appium.webdriver import Remote
from appium.webdriver.common.mobileby import MobileBy as By
from appium.webdriver.common.mobileby import AppiumBy

_url = r'http://127.0.0.1:4723/wd/hub'
_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.zhao.myreader",
    "appActivity": "com.zhao.myreader.ui.home.MainActivity"
}

driver = Remote(_url, _caps)
# 隐式等待3S
driver.implicitly_wait(3)

# 显性等待元素
wait = WebDriverWait(driver, 10)

#
driver.find_element(By.ACCESSIBILITY_ID, '书城').click()
eles = driver.find_elements(By.ID, 'com.zhao.myreader:id/tv_book_name')
eles[0].click()
driver.find_element(By.ID, "com.zhao.myreader:id/btn_read_book").click()
driver.find_element(By.ID, "com.zhao.myreader:id/tv_content").click()
driver.find_element(By.ID, "com.zhao.myreader:id/ll_chapter_list").click()
# print(driver.page_source)

def get_list():
    chapterlist = []
    while True:
        # 显性等待10秒
        eles = wait.until(ec.visibility_of_all_elements_located((By.ID, "com.zhao.myreader:id/tv_chapter_title")))
        if eles[-1].text in chapterlist:
            break
        [chapterlist.append(i.text) for i in eles]
        driver.swipe(364, 851, 364, 333)
    return chapterlist


list1 = get_list()
print(list1)
wait.until(ec.visibility_of_element_located((By.ID, "com.zhao.myreader:id/tv_chapter_sort"))).click()
list2 = get_list()
print(list2)
assert list1 == list2[::-1], "排序失败"
