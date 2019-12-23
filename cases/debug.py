# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from common.common import *
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from page.basepage import *

import time
d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
card = d['data1']['hospital_card']
username = d['data1']['card_user']

elem = get_data('element_data.yaml')

driver = webdriver.Chrome()
page = Page(driver,url)
driver.get(url)
time.sleep(2)
path = (By.XPATH,"//*[contains(text(),'门诊挂号')]")
WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(path)).click()
time.sleep(2)
driver.find_element_by_xpath("//*[contains(text(),'输入就诊卡号')]").click()
time.sleep(2)
driver.find_element_by_class_name('input').send_keys(card)
time.sleep(2)
driver.find_element_by_class_name('confirm-btn').click()
time.sleep(5)
# d = driver.find_elements(By.XPATH, "//*[@class='dept-item']/p")
path = (By.XPATH, "//*[@class='dept-item']/p")
d = page.find_elements(path)
print(d)
if len(d)>0:
    print('-------------')
    print(d[0].text)
    d[0].click()
    print('-------------')
else:
    print('end')
picture = screen_shot(driver, "选择就诊卡类型")
print(picture)
print("-----end-----")


