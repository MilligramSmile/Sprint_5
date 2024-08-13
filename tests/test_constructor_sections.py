from fixtures import BaseTest
from locators import locators


class TestConstructorSections(BaseTest):

    def test_navigate_to_sauce_section(self):
        driver = self.driver
        driver.find_element(*locators["SAUCE_SECTION"]).click()

    def test_navigate_to_filling_section(self):
        driver = self.driver
        driver.find_element(*locators["FILLING_SECTION"]).click()

    def test_navigate_from_sauce_to_bun_section(self):
        driver = self.driver
        driver.find_element(*locators["SAUCE_SECTION"]).click()
        driver.find_element(*locators["BUN_SECTION"]).click()
