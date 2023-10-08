import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.select import Select

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.sec.android.app.popupcalculator',
    appActivity='.Calculator'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
#Click on 1
driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='1']").click()
#Click on the add button
driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Plus']").click()
#Click on 3
driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='3']").click()
#Click on Equal button
driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Equal']").click()
#Click on Clear History
driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Clear history Button']").click()
#Click on Clear Display
driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Clear']").click()

# Sleep for 5 second
time.sleep(5)
#Quit
driver.quit()