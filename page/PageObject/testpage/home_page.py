from page.Page import Page
from common.common import *


d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
card = d['data1']['hospital_card']


class HomePage(Page):
    def __init__(self, driver, base_url=url):
        Page.__init__(self, driver, base_url)

    def HomePage(self):
        print("打开首页:",self.base_url)
        self.driver.get(self.base_url)


