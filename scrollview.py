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

btn_scrollview = driver.find_element(By.ID , 'com.code2lead.kwad:id/ScrollView').click()
time.sleep(2)
btn_1 = driver.find_element(By.XPATH, "//android.widget.Button[@text=\"BUTTON1\"]").click()
txt_alert = driver.find_element(By.ID , 'com.code2lead.kwad:id/alertTitle').is_displayed()
txt_alert_msg = driver.find_element(By.ID , 'android:id/message').text
assert txt_alert_msg == "Are you sure? what to close"
btn_alert_no = driver.find_element(By.ID , 'android:id/button2').click()
driver.swipe(1000, 1600, 1000, 850, 500)
btn_16 = driver.find_element(By.XPATH, "//android.widget.Button[@text=\"BUTTON16\"]").is_displayed()
btn_16 = driver.find_element(By.XPATH, "//android.widget.Button[@text=\"BUTTON16\"]").click()
txt_alert = driver.find_element(By.ID , 'com.code2lead.kwad:id/alertTitle').is_displayed()
txt_alert_msg = driver.find_element(By.ID , 'android:id/message').text
assert txt_alert_msg == "Are you sure? what to close"
btn_alert_yes = driver.find_element(By.ID , 'android:id/button1').click()

time.sleep(2)
print('Success!')
driver.close_app()