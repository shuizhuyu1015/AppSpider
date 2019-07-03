"""
    create by Gray 2019-07-02
"""
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from utils.helper import get_size


cap = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "noReset": True,
    "unicodeKeyboard": True
}


