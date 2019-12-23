from selenium.webdriver.common.by import By
from page.Page import Page
from common.common import *

d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
card = d['data1']['hospital_card']
carduser = d['data1']['card_user']


class RegNumPage(Page):
    reg_num = (By.XPATH, "//*[@class='date-item']")

    def __init__(self, driver, base_url=url):
        Page.__init__(self, driver, base_url)

    def choice_regnum(self):
        num = self.get_regnum()
        if len(num) > 0:
            self.click(num[0])
        else:
            print('-----获取就诊号源-----')

    def get_regnum(self):
        print("-----查看就诊号源------")
        return self.find_elements(self.reg_num)

