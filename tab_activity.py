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

btn_tab_activity = driver.find_element(By.ID , 'com.code2lead.kwad:id/TabView').click()
time.sleep(2)
txt_tab_home = driver.find_element(By.XPATH , "//android.widget.TextView[@text=\"HomeFragment\"]").text
assert txt_tab_home == 'HomeFragment'
btn_tab_sport = driver.find_element(By.ACCESSIBILITY_ID , 'Sport').click()
txt_tab_sport = driver.find_element(By.XPATH , "//android.widget.TextView[@text=\"SportFragment\"]").text
assert txt_tab_sport == 'SportFragment'
btn_tab_movie = driver.find_element(By.ACCESSIBILITY_ID , 'Movie').click()
txt_tab_movie = driver.find_element(By.XPATH , "//android.widget.TextView[@text=\"MovieFragment\"]").text
assert txt_tab_movie == 'MovieFragment'


directory = '%s/screenshot-files/' % os.getcwd()
file_name = 'screenshot_tab_activity.png'
driver.save_screenshot(directory + file_name)

btn_tab_home = driver.find_element(By.ACCESSIBILITY_ID , 'Home').click()
assert txt_tab_home == 'HomeFragment'
btn_tab_activity_back = driver.find_element(By.ACCESSIBILITY_ID , 'Navigate up').click()
time.sleep(2)
print('Success!')
driver.close_app()