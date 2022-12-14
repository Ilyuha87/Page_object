from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.url = url
        self.browser: WebDriver = browser
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
