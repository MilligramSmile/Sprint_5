from locators import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_navigate_to_personal_account(driver):
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
    time.sleep(3)

    assert 'profile' in driver.current_url


def test_navigate_to_constructor(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*locators["CONSTRUCTOR_BUTTON"]).click()
    time.sleep(3)
    p_element = driver.find_element(By.XPATH, '//header//li[1]//p')
    assert p_element.text == "Конструктор", "Текст в заголовке h2 не совпадает с ожидаемым"


def test_navigate_to_logo(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*locators["STELLAR_BURGERS_LOGO"]).click()

    link_element = driver.find_element(*locators["STELLAR_BURGERS_LOGO"])
    link_class = link_element.get_attribute("class")
    assert link_class == "active", "Класс ссылки не совпадает с ожидаемым"
