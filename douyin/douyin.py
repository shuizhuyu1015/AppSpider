"""
    create by Gray 2019-07-02
"""
import re
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from utils.helper import get_size

"""
    1.终端命令查询appPackage
    aapt dump badging apk路径

    2.查询appActivity
    先打开手机中你要获取包名的APP
    adb shell
    dumpsys activity | grep mFocusedActivity
"""


class DouYin:
    cap = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "85GBBMC2375G",
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
        "noReset": True,
        "unicodeKeyboard": True,
        "resetKeyboard": True
    }

    def __init__(self):
        # 调起APP
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', DouYin.cap)
        print('启动抖音')

    def click_search(self):
        # 点击搜索
        print('点击搜索按钮')
        try:
            if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/avl')):
                self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/avl').click()
        except Exception as e:
            print('未找到搜索按钮')

    def login_douyin(self):
        # 如果需要登录则先登录
        print('登录...')
        try:
            if WebDriverWait(self.driver, 2).until(lambda x: x.find_element_by_link_text('密码登录')):
                # 选择密码登录
                self.driver.find_element_by_link_text('密码登录').click()

                if WebDriverWait(self.driver, 1).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/a6s')):
                    self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a6s').send_keys('18666278637')
                    self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a6r').send_keys('shuizhuyu1015')
                    if WebDriverWait(self.driver, 1).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/c0r')):
                        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/c0r').click()
                    self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/nt').click()
                    # 等待8秒，可能要手动输入验证码
                    time.sleep(15)
                    yield
        except Exception as e:
            print('未找到密码登录')

    def if_need_click_teenage_alert(self):
        # 青少年模式弹框
        try:
            if WebDriverWait(self.driver, 1).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/d3_')):
                self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/d_6').click()
                print('取消青少年模式弹框')
        except Exception as e:
            pass

    def input_and_search(self, search_keyword):
        # 点击输入框，输入关键词，并搜索
        print('点击输入框，输入关键词：{}，并搜索'.format(search_keyword))
        try:
            if WebDriverWait(self.driver, 1).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/a9h')):
                self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9h').click()
                self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9h').clear()
                self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/a9h').send_keys(search_keyword)
                # 搜索
                self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/d_s').click()
        except Exception as e:
            print('未找到输入框')

    def click_user_tab(self):
        # 定位到用户Tab
        print('点击用户Tab')
        if WebDriverWait(self.driver, 3).until(
                lambda x: x.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')):
            bar_list = self.driver.find_elements_by_class_name('android.support.v7.app.ActionBar$Tab')
            user_tab = bar_list[2]
            user_tab.click()

    def select_one_user(self, user_id):
        # 点击某个用户
        try:
            if WebDriverWait(self.driver, 3).until(lambda x: x.find_elements_by_id('com.ss.android.ugc.aweme:id/d1u')):
                # 获取所有用户
                users_list = self.driver.find_elements_by_id('com.ss.android.ugc.aweme:id/d1u')
                for user in users_list:
                    re_sear = re.search("抖音号:(.*)", user.text)
                    if re_sear.group(1) == user_id:
                        print('点击用户：{}'.format(user_id))
                        user.click()
                        break
        except Exception as e:
            pass

    def click_fans_tab(self):
        # 点击粉丝
        print('点击粉丝，进入粉丝列表')
        if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/aew')):
            self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/aew').click()
            for i in range(48):
                self.load_more_data()

    def get_current_fans_list(self):
        try:
            if WebDriverWait(self.driver, 3).until(
                    lambda x: x.find_elements_by_xpath(
                        "//android.support.v7.widget.RecyclerView[@resource-id='com.ss.android.ugc.aweme:id/cd0']/android.widget.RelativeLayout")):
                print('获取当前所有粉丝')
                fans_list = self.driver.find_elements_by_xpath(
                    "//android.support.v7.widget.RecyclerView[@resource-id='com.ss.android.ugc.aweme:id/cd0']/android.widget.RelativeLayout")
                print(fans_list)
                self.select_one_fans(fans_list)

        except Exception as e:
            pass

    def select_one_fans(self, all_fans):
        i = 0
        while i < len(all_fans):
            try:
                fans = all_fans[i]
                if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/av4')):
                    print('点击粉丝')
                    fans.find_element_by_id('com.ss.android.ugc.aweme:id/av4').click()
                    time.sleep(1)
                    self.click_more()
                    time.sleep(1)
                    self.click_private_mail()
                    time.sleep(1)
                    self.send_message("关注公众号夏芒铺子，更多母婴知识好物分享，欢迎来撩")
                    time.sleep(1)
                    self.go_back_fans_list()
                    i += 1

            except Exception as e:
                self.load_more_data()
                self.get_current_fans_list()
        else:
            try:
                if self.driver.find_element_by_xpath("//android.widget.TextView[@text='没有更多了~']"):
                    pass
            except Exception as e:
                self.load_more_data()
                self.get_current_fans_list()

    def click_more(self):
        # 点击更多...
        print('点击更多...')
        if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/cwo')):
            self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/cwo').click()

    def click_private_mail(self):
        # 点击私信
        print('点击私信')
        if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/chq')):
            self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/chq').click()
            time.sleep(1)
            # 如果要求安装多闪，点击取消
            try:
                if self.driver.find_element_by_id('android:id/message'):
                    self.driver.find_element_by_id('android:id/button2').click()
            except Exception as e:
                pass

    def send_message(self, msg):
        # 发送私信
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/biw').click()
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/biw').send_keys(msg)
        if WebDriverWait(self.driver, 2).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/chh')):
            print('发送私信：{}'.format(msg))
            self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/chh').click()
            time.sleep(1)

    def go_back_fans_list(self):
        self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/b7j').click()
        if WebDriverWait(self.driver, 1).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/iy')):
            self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/iy').click()
        if WebDriverWait(self.driver, 1).until(lambda x: x.find_element_by_id('com.ss.android.ugc.aweme:id/iy')):
            self.driver.find_element_by_id('com.ss.android.ugc.aweme:id/iy').click()
        print('------返回到粉丝列表------')

    def load_more_data(self):
        # 手势滑动
        print('上推加载更多数据')

        wid, hei = get_size(self.driver)
        x1 = int(wid * 0.5)
        y1 = int(hei * 0.95)
        y2 = int(hei * 0.2)

        self.driver.swipe(x1, y1, x1, y2)
        time.sleep(3)


if __name__ == '__main__':
    douyin = DouYin()
    douyin.click_search()
    douyin.if_need_click_teenage_alert()
    douyin.input_and_search('daddylab')
    douyin.click_user_tab()
    douyin.select_one_user('daddylab')
    douyin.click_fans_tab()
    douyin.get_current_fans_list()

# daddylab
