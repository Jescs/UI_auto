import os
import yaml
from selenium import webdriver
import time
from pathlib import Path


rootpath = os.path.dirname(os.getcwd())


def get_data(file):
    """
    :param file: 传入文件名称
    :return: 读取文件数据
    """
    path = os.path.join(rootpath, 'data')
    filepath = path + '\\' + file
    with open(filepath, 'rb') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


def screen_shot(driver, name):
    """
    :param driver: 传入webdriver
    :param name: 传入图片名称
    :return: 生成图片
    """
    picture_path = os.path.join(rootpath, 'Picture')
    if Path(picture_path).is_dir():
        pass
    else:
        Path(picture_path).mkdir()
    date = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
    picture_name = picture_path+'\\' + name + '  ' + date + '.png'
    driver.get_screenshot_as_file(picture_name)
    return picture_name


if __name__ == '__main__':

    d = get_data('hospital_data.yaml')
    driver = webdriver.Chrome()
    driver.get(d['data1']['hospital_url'])
    screen_shot(driver, 'Index')
