"""Contains configuration fixture for browser."""
import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.base_page import BasePage
from settings import Const


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome, edge, firefox")


@pytest.fixture()
def get_browser(request):
    browser = request.config.getoption('--browser')
    return browser


@pytest.fixture(autouse=True)
def driver(get_browser):
    """Setup and teardown methods for Chrome browser. Used by every test-case."""

    if get_browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    if get_browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function",autouse=True)
def setup(driver):
    page = BasePage(driver)
    page.login(Const.EMAIL, Const.PASSWORD)
