import time
from pathlib import Path
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.select import Select
# str(Path().absolute().parent)+'\\app\\Flipboard.apk'
desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    # appPackage='com.amazon.mShop.android.shopping',
    # appActivity='com.amazon.mShop.navigation.MainActivity'
    app=str(Path().absolute().parent)+'\\apk\\foodpanda.apk'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
#Click on 1
#driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='1']").click()
# Sleep for 5 second
time.sleep(5)
#Quit
driver.quit()

