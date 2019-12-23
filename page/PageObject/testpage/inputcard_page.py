from selenium.webdriver.common.by import By
from page.Page import Page
from common.common import *

d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
card = d['data1']['hospital_card']


class CardInputPage(Page):
    input_card = (By.CLASS_NAME, "input")
    confirm_btn = (By.CLASS_NAME, "confirm-btn")

    def __init__(self, driver, base_url=url):
        Page.__init__(self, driver, base_url)

    def query_card(self, card):
        self.card_input(card)
        self.card_confirm()

    def card_input(self, card_num):
        print("-----输入就诊卡号------")
        return self.input_text(self.input_card, card_num)

    def card_confirm(self):
        print("-----点击确认-----")
        return self.click(self.confirm_btn)
