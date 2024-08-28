from locators import locators


def test_navigate_to_sauce_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*locators["SAUCE_SECTION"]).click()
    h2_element = driver.find_element(*locators["SAUCE_H2"])
    assert h2_element.text == "Соусы", "Текст в заголовке h2 не совпадает с ожидаемым"


def test_navigate_to_filling_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*locators["FILLING_SECTION"]).click()
    h2_element = driver.find_element(*locators["FILLING_H2"])
    assert h2_element.text == "Начинки", "Текст в заголовке h2 не совпадает с ожидаемым"


def test_navigate_from_sauce_to_bun_section(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*locators["SAUCE_SECTION"]).click()
    driver.find_element(*locators["BUN_SECTION"]).click()
    h2_element = driver.find_element(*locators["BUN_H2"])
    assert h2_element.text == "Булки", "Текст в заголовке h2 не совпадает с ожидаемым"
