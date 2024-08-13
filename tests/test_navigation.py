from fixtures import BaseTest
from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNavigation(BaseTest):

    def test_navigate_to_personal_account(self):

        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.find_element(*locators["ACCOUNT_BUTTON"]).click()
        email_field = wait.until(EC.presence_of_element_located(locators["EMAIL_FIELD"]))
        email_field.send_keys("demo12345@yandex.ru")

        password_field = wait.until(EC.presence_of_element_located(locators["PASSWORD_FIELD"]))
        password_field.send_keys("demo12345")

        login_button = wait.until(EC.element_to_be_clickable(locators["LOGIN_BUTTON"]))
        login_button.click()

        personal_account_button = wait.until(EC.element_to_be_clickable(locators["PERSONAL_ACCOUNT_BUTTON"]))
        personal_account_button.click()

    def test_navigate_to_constructor(self):
        driver = self.driver
        driver.find_element(*locators["CONSTRUCTOR_BUTTON"]).click()
        self.assertTrue(driver.find_element(By.XPATH, '//h1[text()="Соберите бургер"]').is_displayed())

        driver.find_element(*locators["STELLAR_BURGERS_LOGO"]).click()
        self.assertTrue(driver.find_element(By.XPATH, '//h1[text()="Соберите бургер"]').is_displayed())
