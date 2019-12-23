from selenium.webdriver.common.by import By
from selenium import webdriver
from page.basepage import Page
from common.common import *
import allure

d = get_data('hospital_data.yaml')
url = d['data1']['hospital_url']
card = d['data1']['hospital_card']
elem = get_data('element_data.yaml')


class RegisterCase(Page):
    reg_path = (By.XPATH, "//*[contains(text(),'门诊挂号')]")
    enter_card = (By.XPATH, "//*[contains(text(),'输入就诊卡号')]")
    input_card = (By.CLASS_NAME, "input")
    confirm_btn = (By.CLASS_NAME, "confirm-btn")
    dept = (By.XPATH, "//*[@class='dept-item']/p")
    username = (By.CLASS_NAME, "username")
    next_page = (By.CLASS_NAME, "next-page")
    date = (By.XPATH, "//*[@class='date-item']/strong")
    am_pm = (By.XPATH, "//*[@class='am-item']/span")
    doc_list = (By.XPATH, "//*[@class='doctor-item']")
    reg_num = (By.XPATH, "//*[@class='date-item']")
    confirm_reg = (By.XPATH, "//*[@class='userinfo-item'][2]/p[2]")

    def __init__(self, driver, base_url=url):
        Page.__init__(self, driver, base_url)

    @allure.step("-----打开首页-----")
    def home(self):
        try:
            print("打开首页:", self.base_url)
            picture = screen_shot(self.driver, "自助机首页")
            allure.attach.file(picture, "自助机首页", attachment_type=allure.attachment_type.PNG)
            self.index()
        except Exception as msg:
            picture = screen_shot(self.driver, "打开首页失败")
            allure.attach.file(picture, "打开首页失败", attachment_type=allure.attachment_type.PNG)
            print("-----打开首页失败:{}------".format(msg))
            raise

    # def register(self, card):
    #     self.driver.get(self.base_url)
    #     picture = screen_shot(self.driver, "自助机首页")
    #     allure.attach.file(picture,"自助机首页", attachment_type=allure.attachment_type.PNG)
    #     time.sleep(5)
    #     self.register_click()
    #     picture = screen_shot(self.driver, "选择就诊卡类型")
    #     allure.attach.file(picture, "选择就诊卡类型", attachment_type=allure.attachment_type.PNG)
    #     time.sleep(5)
    #     self.input_card_click()
    #     picture = screen_shot(self.driver, "输入就诊卡")
    #     allure.attach.file(picture, "输入就诊卡", attachment_type=allure.attachment_type.PNG)
    #     time.sleep(7)
    #     self.card_input(card)
    #     self.card_confirm()
    #     picture = screen_shot(self.driver, "查询科室")
    #     allure.attach.file(picture, "查询科室", attachment_type=allure.attachment_type.PNG)
    #     time.sleep(7)
    #     self.get_depts()
    #     picture = screen_shot(self.driver, "查询就诊日期")
    #     allure.attach.file(picture, "查询就诊日期", attachment_type=allure.attachment_type.PNG)
    #     time.sleep(7)
    #     self.get_date()
    #     picture = screen_shot(self.driver, "选择就诊上下午")
    #     allure.attach.file(picture, "选择就诊上下午", attachment_type=allure.attachment_type.PNG)
    #     time.sleep(7)
    #     self.get_am()
    #     picture = screen_shot(self.driver, "查询就诊医生")
    #     allure.attach.file(picture, "查询就诊医生", attachment_type=allure.attachment_type.PNG)
    #     time.sleep(7)
    #     self.get_docs()
    #     picture = screen_shot(self.driver, "查询剩余号源")
    #     allure.attach.file(picture, "查询剩余号源", attachment_type=allure.attachment_type.PNG)
    #     time.sleep(7)
    #     self.get_regnum()
    #     picture = screen_shot(self.driver, "锁号")
    #     allure.attach.file(picture, "锁号", attachment_type=allure.attachment_type.PNG)
    #     time.sleep(5)
    #     self.get_confirm_reg()

    @allure.step("-----点击门诊挂号-----")
    def register_click(self):
        print("-----点击门诊挂号-----")
        self.click(self.reg_path)

    @allure.step("-----点击输入就诊卡号-----")
    def input_card_click(self):
        print("-----点击输入就诊卡号-----")
        picture = screen_shot(self.driver, "选择就诊卡类型")
        allure.attach.file(picture, "选择就诊卡类型", attachment_type=allure.attachment_type.PNG)
        self.click(self.enter_card)

    @allure.step("-----输入就诊卡号-----")
    def card_input(self, card_num):
        print("-----输入就诊卡号------")
        picture = screen_shot(self.driver, "输入就诊卡")
        allure.attach.file(picture, "输入就诊卡", attachment_type=allure.attachment_type.PNG)
        return self.input_text(self.input_card, card_num)

    @allure.step("-----点击确认-----")
    def card_confirm(self):
        try:
            print("-----点击确认-----")
            return self.click(self.confirm_btn)
        except Exception as msg:
            picture = screen_shot(self.driver, "点击确认失败")
            allure.attach.file(picture, "点击确认失败", attachment_type=allure.attachment_type.PNG)
            print("-----点击确认失败:{}------".format(msg))
            raise

    @allure.step("-----查看就诊科室-----")
    def get_depts(self):
        try:
            picture = screen_shot(self.driver, "查询科室")
            allure.attach.file(picture, "查询科室", attachment_type=allure.attachment_type.PNG)
            print("-----查看就诊科室------")
            self.get_elements(self.dept)
        except Exception as msg:
            picture = screen_shot(self.driver, "查询科室失败")
            allure.attach.file(picture, "查询科室失败", attachment_type=allure.attachment_type.PNG)
            print("-----查询科室失败:{}------".format(msg))
            raise

    @allure.step("-----获取就诊卡姓名-----")
    def get_username(self):
        try:
            print("-----获取就诊卡姓名-----")
            return self.get_text(self.username)
        except Exception as msg:
            picture = screen_shot(self.driver, "获取就诊卡姓名失败")
            allure.attach.file(picture, "获取就诊卡姓名失败", attachment_type=allure.attachment_type.PNG)
            print("-----获取就诊卡姓名失败:{}------".format(msg))
            raise

    @allure.step("-----查看时间-----")
    def get_date(self):
        try:
            print("-----查看时间------")
            picture = screen_shot(self.driver, "查询就诊日期")
            allure.attach.file(picture, "查询就诊日期", attachment_type=allure.attachment_type.PNG)
            self.get_elements(self.date)
        except Exception as msg:
            picture = screen_shot(self.driver, "查询就诊日期失败")
            allure.attach.file(picture, "查询就诊日期失败", attachment_type=allure.attachment_type.PNG)
            print("-----查询就诊日期失败:{}------".format(msg))
            raise

    @allure.step("-----选择上下午-----")
    def get_am(self):
        try:
            print("-----选择上下午------")
            picture = screen_shot(self.driver, "选择就诊上下午")
            allure.attach.file(picture, "选择就诊上下午", attachment_type=allure.attachment_type.PNG)
            self.get_elements(self.am_pm)
        except Exception as msg:
            picture = screen_shot(self.driver, "选择就诊上下午失败")
            allure.attach.file(picture, "选择就诊上下午失败", attachment_type=allure.attachment_type.PNG)
            print("-----选择就诊上下午失败:{}------".format(msg))
            raise

    @allure.step("-----查看就诊医生-----")
    def get_docs(self):
        try:
            picture = screen_shot(self.driver, "查询就诊医生")
            allure.attach.file(picture, "查询就诊医生", attachment_type=allure.attachment_type.PNG)
            print("-----查看就诊医生------")
            self.get_elements(self.doc_list)
        except Exception as msg:
            picture = screen_shot(self.driver, "查询就诊医生失败")
            allure.attach.file(picture, "查询就诊医生失败", attachment_type=allure.attachment_type.PNG)
            print("-----查询就诊医生失败:{}------".format(msg))
            raise

    @allure.step("-----查看就诊号源-----")
    def get_regnum(self):
        try:
            print("-----查看就诊号源------")
            self.get_elements(self.reg_num)
            picture = screen_shot(self.driver, "查询剩余号源")
            allure.attach.file(picture, "查询剩余号源", attachment_type=allure.attachment_type.PNG)
        except Exception as msg:
            picture = screen_shot(self.driver, "查询剩余号源失败")
            allure.attach.file(picture, "查询剩余号源失败", attachment_type=allure.attachment_type.PNG)
            print("-----查询剩余号源失败:{}------".format(msg))
            raise

    @allure.step("-----确认挂号信息-----")
    def get_confirm_reg(self):
        try:
            picture = screen_shot(self.driver, "锁号")
            allure.attach.file(picture, "锁号", attachment_type=allure.attachment_type.PNG)
            print("-----确认挂号信息------")
            return self.get_text(self.confirm_reg)
        except Exception as msg:
            picture = screen_shot(self.driver, "锁号失败")
            allure.attach.file(picture, "锁号失败", attachment_type=allure.attachment_type.PNG)
            print("-----锁号失败:{}------".format(msg))
            raise


if __name__ == '__main__':
    driver = webdriver.Chrome()
    test = RegisterCase(driver)

