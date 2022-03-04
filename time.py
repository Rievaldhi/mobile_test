from appium import webdriver
from selenium.webdriver.common.by import By
import time
import os

desired_cap = {}

desired_cap['platformName'] = 'Android'
desired_cap['deviceName'] = 'mtest'
desired_cap['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_cap['appPackage'] = 'com.code2lead.kwad'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub' , desired_cap)
driver.implicitly_wait(10)

driver.swipe(1000, 1600, 1000, 850, 500)
btn_time = driver.find_element(By.ID , 'com.code2lead.kwad:id/Time').click()
#select hours
hours_picker = driver.find_element(By.ID , 'android:id/hours').is_displayed()
hours_10 = driver.find_element(By.ACCESSIBILITY_ID , '10').click()
minutes_picker = driver.find_element(By.ID , 'android:id/minutes').click()
minutes_25 = driver.find_element(By.ACCESSIBILITY_ID , '25').click()
pm_picker = driver.find_element(By.ID , 'android:id/pm_label').click()

directory = '%s/screenshot-files/' % os.getcwd()
file_name = 'screenshot_time.png'
driver.save_screenshot(directory + file_name)

time.sleep(2)
print('Success!')
driver.close_app()