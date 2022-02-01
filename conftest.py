"""Contains configuration fixture for browser."""
import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from msedge.selenium_tools import EdgeOptions, Edge
from pages.base_page import BasePage
from settings import Const


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome, edge, firefox.")
    parser.addoption("--headless", action='store', default='off', help='headless browser: on or off.')


@pytest.fixture
def get_browser(request):
    browser = request.config.getoption('--browser')
    return browser


@pytest.fixture
def headless_mode(request):
    headless_mode = request.config.getoption('--headless')
    return headless_mode


@pytest.fixture(autouse=True)
def driver(get_browser, headless_mode):
    """Setup and teardown methods for Chrome browser. Used by every test-case."""

    if get_browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        if headless_mode == "on":
            options.add_argument("--headless")
        else:
            pass
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    if get_browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        if headless_mode == "on":
            options.add_argument("--headless")
        else:
            pass
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    if get_browser == "edge":
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        if headless_mode == "on":
            options.add_argument("headless")
        else:
            pass
        #options.binary_location = r"/usr/bin/microsoft-edge-dev"
        options.set_capability("platform", "LINUX")

        driver = Edge(options=options, executable_path='/usr/local/bin/msedgedriver')

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def login(driver):
    page = BasePage(driver)
    page.login(Const.EMAIL, Const.PASSWORD)
