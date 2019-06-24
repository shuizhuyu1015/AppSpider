"""
    create by Gray 2019-06-22
"""
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


cap = {
    "platformName": "Android",
    "platformVersion": "4.4.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
    "noReset": True,
    "unicodeKeyboard": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", cap)


def get_size():
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    return width, height


try:

    if WebDriverWait(driver, 2).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']")):
        # 如果出现跳过按钮才点击
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']").click()
except Exception as e:
    print(e)

try:
    if WebDriverWait(driver, 2).until(lambda x: x.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")):
        # 如果出现用户名框，则输入账号密码登录
        driver.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys(
            '天行哥')
        driver.find_element_by_xpath(
            "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']").send_keys(
            'shuizhuyu1015')
        driver.find_element_by_xpath(
            "//android.widget.Button[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()
except Exception as e:
    print(e)

if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath(
            "//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]")):
    # 点击研讯
    driver.find_element_by_xpath(
        "//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()

    time.sleep(1)

    # 手势滑动
    wid, hei = get_size()

    x1 = int(wid * 0.5)
    y1 = int(hei * 0.75)
    y2 = int(hei * 0.25)

    while True:
        driver.swipe(x1, y1, x1, y2)
        time.sleep(1.5)
