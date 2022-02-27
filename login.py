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

btn_login = driver.find_element(By.ID , 'com.code2lead.kwad:id/Login').click()
time.sleep(2)
txt_login_page = driver.find_element(By.XPATH , "//android.widget.TextView[@text=\"Login Page\"]").text
assert txt_login_page == 'Login Page'
f_email_login = driver.find_element(By.ID , 'com.code2lead.kwad:id/Et4').send_keys('admin@gmail.com')
f_pass_login = driver.find_element(By.ID , 'com.code2lead.kwad:id/Et5').send_keys('admin123')
btn_login_page = driver.find_element(By.ID , 'com.code2lead.kwad:id/Btn3').click()
time.sleep(2)

directory = '%s/screenshot-files/' % os.getcwd()
file_name = 'screenshot_after_login.png'
driver.save_screenshot(directory + file_name)

content_edit_admin = 'New Admin Here!'
f_edit_admin = driver.find_element(By.ID , 'com.code2lead.kwad:id/Edt_admin').send_keys(content_edit_admin)
btn_submit_login = driver.find_element(By.ID , 'com.code2lead.kwad:id/Btn_admin_sub').click()
result_edit_admin = driver.find_element(By.ID , 'com.code2lead.kwad:id/Tv_admin').text
assert result_edit_admin == content_edit_admin

file_name1 = 'screenshot_after_edit.png'
driver.save_screenshot(directory + file_name1)

time.sleep(2)
print('Success!')
driver.close_app()

