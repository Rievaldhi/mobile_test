from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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
btn_date = driver.find_element(By.ID , 'com.code2lead.kwad:id/Date').click()
#select date
year_select = driver.find_element(By.ID , 'android:id/date_picker_header_year').click()

year_current = driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"1990\"]")
year_selected_1990 = driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"1990\"]")

try:
    driver.find_element(By.XPATH , "//android.widget.TextView[@text=\"1990\"]")
except NoSuchElementException:
        driver.swipe(805, 845, 830, 1530)
        print('do scrolling')
year_1990.click()
print('selected years found')

# if  year_1990 != year_current:
#     driver.swipe(805, 845, 830, 1530)
#     print('do scrolling')
# else:
#     year_1990.click()
#     print('selected years found')

# if year_1990 == 1990:
#     year_1990.click()
#     print('selected years found')
# else:
#     driver.swipe(805, 845, 830, 1530)
#     print('do scrolling')
    
date_select = driver.find_element(By.ACCESSIBILITY_ID , '20 April 1990' ).click()
assert date_select == '20 April 1990'

directory = '%s/screenshot-files/' % os.getcwd()
file_name = 'screenshot_date.png'
driver.save_screenshot(directory + file_name)

time.sleep(2)
print('Success!')
driver.close_app()