from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_logout(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*locators["ACCOUNT_BUTTON"]).click()
    email_field = wait.until(EC.presence_of_element_located(locators["EMAIL_FIELD"]))
    email_field.send_keys("demo12345@yandex.ru")

    password_field = wait.until(EC.presence_of_element_located(locators["PASSWORD_FIELD"]))
    password_field.send_keys("demo12345")

    login_button = wait.until(EC.element_to_be_clickable(locators["LOGIN_BUTTON"]))
    login_button.click()

    personal_account_button = wait.until(EC.element_to_be_clickable(locators["PERSONAL_ACCOUNT_BUTTON"]))
    personal_account_button.click()

    logout_button = wait.until(EC.element_to_be_clickable(locators["LOGOUT_BUTTON"]))
    logout_button.click()
    time.sleep(3)
    assert 'login' in driver.current_url
