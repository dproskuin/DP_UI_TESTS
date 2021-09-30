"""Contains configuration fixture for browser."""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    """ Add custom options for CMD here. """
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture
def get_browser(request):
    """ Obtain URL with chosen environment. """
    browser = request.config.getoption("browser")

    if browser == "chrome" or "Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)

    if browser == "firefox" or "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.implicitly_wait(10)

    else:
        raise pytest.UsageError(
            "--browser option is invalid. Supported browsers: Chrome, Firefox")
    return driver


@pytest.fixture(autouse=True)
def driver():
    """Setup and teardown methods for Chrome browser. Used by every test-case."""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
