from selenium.webdriver.common.by import By
from page.Page import Page
from common.common import *

d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
card = d['data1']['hospital_card']
carduser = d['data1']['card_user']


class DeptPage(Page):
    dept = (By.XPATH, "//*[@class='dept-item']/p")
    username = (By.CLASS_NAME, "username")
    next_page = (By.CLASS_NAME, "next-page")

    def __init__(self, driver, base_url=url):
        Page.__init__(self, driver, base_url)

    def choice_dept(self):
        depts = self.get_depts(self.dept)
        if len(depts) > 0:
            self.click(depts[0])
        else:
            print('-----获取科室失败-----')

    def confirm_username(self):
        assert self.get_username() == carduser

    def get_depts(self):
        print("-----查看就诊科室------")
        return self.find_elements(self.dept)

    def get_username(self):
        print("-----获取就诊卡姓名-----")
        return self.get_text(self.username)