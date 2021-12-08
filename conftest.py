"""Contains configuration fixture for browser."""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage


@pytest.fixture(autouse=True)
def driver():
    """Setup and teardown methods for Chrome browser. Used by every test-case."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    #options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function",autouse=True)
def setup(driver):
    page = BasePage(driver)
    page.login()
