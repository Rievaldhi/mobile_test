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

btn_contact_us = driver.find_element(By.ID , 'com.code2lead.kwad:id/ContactUs').click()
time.sleep(2)
content_name = 'Rievaldhi'
f_enter_name = driver.find_element(By.ID , 'com.code2lead.kwad:id/Et2').send_keys(content_name)
content_email = 'rievaldhi.test@gmail.com'
f_enter_email = driver.find_element(By.ID , 'com.code2lead.kwad:id/Et3').send_keys(content_email)
content_address = 'Jawa Barat'
f_enter_address = driver.find_element(By.ID , 'com.code2lead.kwad:id/Et6').send_keys(content_address)
content_mobNo = '089711111111'
f_enter_mobileNo = driver.find_element(By.ID , 'com.code2lead.kwad:id/Et7').send_keys(content_mobNo)
time.sleep(3)
btn_submit_contact_us = driver.find_element(By.ID , 'com.code2lead.kwad:id/Btn2').click()

result_name = driver.find_element(By.ID , 'com.code2lead.kwad:id/Tv2').text
result_email = driver.find_element(By.ID , 'com.code2lead.kwad:id/Tv7').text
result_pass = driver.find_element(By.ID , 'com.code2lead.kwad:id/Tv5').text
result_mobile = driver.find_element(By.ID , 'com.code2lead.kwad:id/Tv6').text


assert result_name == "Name: " + content_name
assert result_email == "Email: " + content_email
assert result_pass == "Password: " + content_address
assert result_mobile == "Mobile: " + content_mobNo

time.sleep(2)
print('Success!')
driver.close_app()
