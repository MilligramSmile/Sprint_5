import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()  # Или используйте webdriver.Firefox() для Firefox
    yield driver
    driver.quit()