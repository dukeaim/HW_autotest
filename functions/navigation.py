# coding=utf-8
from time import sleep
import settings

class Navigation:

    _driver = None
    _url = ''

    def __init__(self, driver, url=''):
        self._driver = driver
        self._url = url

    def to_index_page(self):
        self._driver.get(self._url)

    def search(self, text):
        elem = self._driver.find_element_by_name('q')
        elem.clear()
        elem.send_keys(text)
        elem.submit()
        sleep(3)

    def create_comment(self):
        # находим ссылку у первого текстового поста
        elem = self._driver.find_element_by_xpath("//div[@class='story'][0]/"
                                                  "div[@class='story__main]/div[@class='story__header]/"
                                                  "div[@class='story__header-title]/a")
        self._driver.get(elem.get_attribute('href'))
        textbox = self._driver.find_element_by_xpath("//div[contains(@class, 'b-comments-reply__editable')][0]")
        text_message = settings.MESSAGE_TEXT
        textbox.send_keys(text_message)
        textbox.submit()
        sleep(2)
        return text_message in self._driver.page_source
