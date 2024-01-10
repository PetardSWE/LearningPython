from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

url = 'https://---.se/prod/ollpp01/komoga/KoGDefault.aspx'
timestamp = datetime.now().strftime("%H:%M")
driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get(url)
driver.find_element(By.XPATH,'//*[@id="ivRadioPersonnrLogin"]').click()
driver.find_element(By.XPATH,'//*[@id="ivTxtFlexId"]').send_keys('username')
driver.find_element(By.XPATH,'//*[@id="ivBtnOk"]').click()
driver.find_element(By.XPATH,'//*[@id="ivBtnUt"]').click()
time.sleep(3)
driver.close()

print("\nDu är nu utstämplad klockan {timestamp}, ha en bra eftermiddag!")
