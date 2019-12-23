from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from common.common import *


class Page(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def index(self):
        self.driver.get(self.base_url)

    def find_element(self, loc):
        return WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(loc))
        # return self.driver.find_element(*loc)

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def click(self, loc):
        self.find_element(loc).click()

    def get_title(self):
        return self.driver.title

    def find_elements(self, loc):
        return WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_all_elements_located(loc))

    def get_text(self, *loc):
        return self.driver.find_element(*loc).text()

    def get_elements(self, loc):
        locs = self.find_elements(loc)
        if len(locs)>0:
            print(locs[0].text)
            return locs[0].click()
        else:
            print('-----fail-----')
            raise Exception


if __name__ == '__main__':
    driver = webdriver.Chrome()
    d = get_data('hospital_data.yaml')
    url = d['data1']['hospital_url']
    page = Page(driver,url)
    page.index()
    reg_path = (By.XPATH, "//*[contains(text(),'门诊挂号')]")
    page.click(reg_path)

