import unittest
from fixtures import BaseTest
from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import generate_name, generate_login, generate_password


class TestRegistration(BaseTest):

    def test_successful_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.find_element(*locators["ACCOUNT_BUTTON"]).click()
        driver.find_element(*locators["REGISTER_LINK"]).click()

        name = generate_name()
        email = generate_login()
        password = generate_password()

        name_field = wait.until(EC.presence_of_element_located(locators["NAME_FIELD"]))
        name_field.send_keys(name)

        email_field = wait.until(EC.presence_of_element_located(locators["EMAIL_FIELD"]))
        email_field.send_keys(email)

        password_field = wait.until(EC.presence_of_element_located(locators["PASSWORD_FIELD"]))
        password_field.send_keys(password)

        register_button = wait.until(EC.element_to_be_clickable(locators["REGISTER_BUTTON"]))
        register_button.click()

    def test_registration_with_invalid_password(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.find_element(*locators["ACCOUNT_BUTTON"]).click()
        driver.find_element(*locators["REGISTER_LINK"]).click()

        name = generate_name()
        email = generate_login()

        name_field = wait.until(EC.presence_of_element_located(locators["NAME_FIELD"]))
        name_field.send_keys(name)

        email_field = wait.until(EC.presence_of_element_located(locators["EMAIL_FIELD"]))
        email_field.send_keys(email)

        password_field = wait.until(EC.presence_of_element_located(locators["PASSWORD_FIELD"]))
        password_field.send_keys("123")

        register_button = wait.until(EC.element_to_be_clickable(locators["REGISTER_BUTTON"]))
        register_button.click()

        error_message = wait.until(
            EC.presence_of_element_located((By.XPATH, '//p[text()="Некорректный пароль"]'))
        )
        self.assertTrue(error_message.is_displayed())
