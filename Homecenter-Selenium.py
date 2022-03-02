from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\webdrivers\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.homecenter.co.il/')

link = driver.find_element(By.LINK_TEXT,'שלום אורח התחבר')
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'userName'))
    )

    user_name = driver.find_element(By.ID,'userName')
    user_name.send_keys('user1')

    password = driver.find_element(By.ID,'userPassword')
    password.send_keys('1234')

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'שכחת סיסמא?'))
    )
    element.click()

except:
    driver.implicitly_wait(5)

#       *** IN PROGRESS ***




