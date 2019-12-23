from selenium.webdriver.common.by import By
from page.Page import Page
from common.common import *

d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
card = d['data1']['hospital_card']
carduser = d['data1']['card_user']


class DatePage(Page):
    date = (By.XPATH, "//*[@class='date-item']/strong")
    am_pm = (By.XPATH, "//*[@class='am-item']/span")

    def __init__(self, driver, base_url=url):
        Page.__init__(self, driver, base_url)

    def choice_date(self):
        dates = self.get_date()
        if len(dates) > 0:
            self.click(dates[0])
        else:
            print('-----获取就诊日期失败-----')

    def choice_am(self):
        ams = self.get_am()
        if len(ams) > 0:
            self.click(ams[0])
        else:
            print('-----获取上下午失败-----')

    def get_date(self):
        print("-----查看时间------")
        return self.find_elements(self.date)

    def get_am(self):
        print("-----选择上下午------")
        return self.find_elements(self.am_pm)

