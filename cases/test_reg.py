from page.register_case import *
from common.common import *
import allure
import pytest
import unittest

d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
elem = get_data('element_data.yaml')
card = d['data1']['hospital_card']


@allure.feature("挂号流程测试")
class Test_Register(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.page = RegisterCase(cls.driver)
        cls.base_url = url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('测试挂号')
    @allure.story("测试挂号流程")
    def test_register_01(self):
        self.page.home()
        time.sleep(5)
        self.page.register_click()
        time.sleep(5)
        self.page.input_card_click()
        time.sleep(7)
        self.page.card_input(card)
        self.page.card_confirm()
        time.sleep(7)
        self.page.get_depts()
        time.sleep(7)
        self.page.get_date()
        time.sleep(7)
        self.page.get_am()
        time.sleep(7)
        self.page.get_docs()
        time.sleep(7)
        self.page.get_regnum()
        time.sleep(5)
        self.page.get_confirm_reg()


if __name__ == '__main__':
    pytest.main(["-q", "test_reg.py"])
