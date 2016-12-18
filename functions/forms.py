# coding=utf-8
from time import sleep
from functions import Navigation
import settings


class Forms:
    _driver = None

    def __init__(self, driver):
        self._driver = driver

    def search(self, text):
        Navigation(self._driver).search(text)
        return u'Посты не найдены' not in self._driver.page_source

    def authorization(self, login, passwd):
        elem = self._driver.find_element_by_name('user')
        elem.clear()
        elem.send_keys(login)
        elem = self._driver.find_element_by_name('passwd')
        elem.clear()
        elem.send_keys(passwd)
        elem.submit()
        sleep(1)
        return u'Настройки' in self._driver.page_source

    def valid_authorization(self):
        self.authorization(settings.LOGIN, settings.PASSWORD)
        sleep(2)
