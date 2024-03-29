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

btn_enter_value = driver.find_element(By.ID , 'com.code2lead.kwad:id/EnterValue').click()
time.sleep(2)
content1 = 'Ini adalah kalimat '
f_enter_value = driver.find_element(By.ID , 'com.code2lead.kwad:id/Et1').send_keys(content1)
time.sleep(2)
assert f_enter_value.text == content1
btn_submit_value = driver.find_element(By.ID , 'com.code2lead.kwad:id/Btn1').click()

directory = '%s/screenshot-files/' % os.getcwd()
file_name = 'screenshot_enter_value.png'
driver.save_screenshot(directory + file_name)

time.sleep(5)
print('Success!')
driver.close_app()