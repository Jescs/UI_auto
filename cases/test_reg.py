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
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = RegisterCase(self.driver)
        self.base_url = url

    def teardowm(self):
        self.driver.quit()

    @allure.title('测试挂号')
    @allure.story("测试挂号流程")
    def test_register_01(self):
        self.driver.get(self.base_url)
        picture = screen_shot(self.driver, "自助机首页")
        allure.attach.file(picture, "自助机首页", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        self.page.register_click()
        picture = screen_shot(self.driver, "选择就诊卡类型")
        allure.attach.file(picture, "选择就诊卡类型", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        self.page.input_card_click()
        picture = screen_shot(self.driver, "输入就诊卡")
        allure.attach.file(picture, "输入就诊卡", attachment_type=allure.attachment_type.PNG)
        time.sleep(7)
        self.page.card_input(card)
        self.page.card_confirm()
        picture = screen_shot(self.driver, "查询科室")
        allure.attach.file(picture, "查询科室", attachment_type=allure.attachment_type.PNG)
        time.sleep(7)
        self.page.get_depts()
        picture = screen_shot(self.driver, "查询就诊日期")
        allure.attach.file(picture, "查询就诊日期", attachment_type=allure.attachment_type.PNG)
        time.sleep(7)
        self.page.get_date()
        picture = screen_shot(self.driver, "选择就诊上下午")
        allure.attach.file(picture, "选择就诊上下午", attachment_type=allure.attachment_type.PNG)
        time.sleep(7)
        self.page.get_am()
        picture = screen_shot(self.driver, "查询就诊医生")
        allure.attach.file(picture, "查询就诊医生", attachment_type=allure.attachment_type.PNG)
        time.sleep(7)
        self.page.get_docs()
        picture = screen_shot(self.driver, "查询剩余号源")
        allure.attach.file(picture, "查询剩余号源", attachment_type=allure.attachment_type.PNG)
        time.sleep(7)
        self.page.get_regnum()
        picture = screen_shot(self.driver, "锁号")
        allure.attach.file(picture, "锁号", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        self.page.get_confirm_reg()


if __name__ == '__main__':
    pytest.main(["-q", "test_reg.py"])
