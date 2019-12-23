from selenium.webdriver.common.by import By
from page.Page import Page
from common.common import *

d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
card = d['data1']['hospital_card']
carduser = d['data1']['card_user']


class ConfirmPage(Page):
    confirm_reg = (By.XPATH, "//*[@class='userinfo-item'][2]/p[2]")

    def __init__(self, driver, base_url=url):
        Page.__init__(self, driver, base_url)

    def conf_reg(self):
        text = self.get_confirm_reg()
        if text == '':
            print("-----确认挂号信息失败------")

    def get_confirm_reg(self):
        print("-----确认挂号信息------")
        return self.get_text(self.confirm_reg)

