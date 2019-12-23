from selenium.webdriver.common.by import By
from page.Page import Page
from common.common import *

d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
card = d['data1']['hospital_card']


class CardtypePage(Page):
    entity_card = (By.XPATH, "//*[contains(text(),'实体就诊卡')]")
    input_card = (By.XPATH, "//*[contains(text(),'输入就诊卡号')]")
    electric_card = (By.XPATH, "//*[contains(text(),'电子就诊卡')]")

    def __init__(self, driver, base_url=url):
        Page.__init__(self, driver, base_url)

    def electric_card_click(self):
        print("-----点击电子就诊卡-----")
        self.click(self.electric_card)

    def entity_card_click(self):
        print("-----点击实体就诊卡-----")
        self.click(self.entity_card)

    def input_card_click(self):
        print("-----点击输入就诊卡号-----")
        self.click(self.input_card)
