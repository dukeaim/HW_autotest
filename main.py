from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import manager
import os


if __name__ == '__main__':
    binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary)
    try:
        if not os.path.isfile('settings.py'):
            raise Exception('Not found settings!')
        manager.start(driver)
    finally:
        driver.quit()
