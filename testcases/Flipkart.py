import time
from pathlib import Path
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
    appPackage='com.flipkart.android',
    appActivity='com.flipkart.android.SplashActivity'

     #app=str(Path().absolute().parent)+'\\apk\\flipkart.apk'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
#Click on 1
driver.find_element(By.ID,"com.flipkart.android:id/custom_back_icon").click()
time.sleep(10)
driver.find_element(By.XPATH, "//android.widget.TextView[@text='Search for products']").click()

# Sleep for 5 second
time.sleep(5)
#Quit
driver.quit()

