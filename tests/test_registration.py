from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import generate_name, generate_login, generate_password


def test_successful_registration(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://stellarburgers.nomoreparties.site/")
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

    assert 'https://stellarburgers.nomoreparties.site/' in driver.current_url


def test_registration_with_invalid_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
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

    assert 'register' in driver.current_url
