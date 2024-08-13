import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        browser = 'chrome'  # Можно поменять на 'firefox'
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser!")

        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
