from selenium.webdriver.common.by import By

locators = {
    "ACCOUNT_BUTTON": (By.XPATH, '//button[text()="Войти в аккаунт"]'),
    "REGISTER_LINK": (By.XPATH, '//a[text()="Зарегистрироваться"]'),
    "NAME_FIELD": (By.XPATH, '//fieldset[1]//input[@name="name"]'),
    "EMAIL_FIELD": (By.XPATH, '//fieldset[last()-1]//input[@name="name"]'),
    "PASSWORD_FIELD": (By.XPATH, '//input[@name="Пароль"]'),
    "REGISTER_BUTTON": (By.XPATH, '//button[text()="Зарегистрироваться"]'),
    "LOGIN_BUTTON": (By.XPATH, '//button[text()="Войти"]'),
    "PERSONAL_ACCOUNT_BUTTON": (By.XPATH, '//nav/a'),
    "LOGOUT_BUTTON": (By.XPATH, '//li/button[text()="Выход"]'),
    "CONSTRUCTOR_BUTTON": (By.XPATH, '//header//li[1]/a'),
    "STELLAR_BURGERS_LOGO": (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'),

    "BUN_SECTION": (By.XPATH, '//span[text()="Булки"]'),
    "SAUCE_SECTION": (By.XPATH, '//span[text()="Соусы"]'),
    "FILLING_SECTION": (By.XPATH, '//span[text()="Начинки"]'),
}