from selenium.webdriver.common.by import By
from page.Page import Page
from common.common import *

d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
card = d['data1']['hospital_card']
carduser = d['data1']['card_user']


class DocListPage(Page):
    doc_list = (By.XPATH, "//*[@class='doctor-item']")

    def __init__(self, driver, base_url=url):
        Page.__init__(self, driver, base_url)

    def choice_doc(self):
        docs = self.get_docs()
        if len(docs) > 0:
            self.click(docs[0])
        else:
            print('-----获取医生失败-----')

    def get_docs(self):
        print("-----查看就诊医生------")
        return self.find_elements(self.doc_list)

