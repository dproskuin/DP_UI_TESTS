"""This module describes Base page methods (Page object)."""
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.common.by import By
from settings import Const, Urls

class LoginPageLocators:
    SIGN_IN_BUTTON_HEADER = (By.CSS_SELECTOR, ".glZmJR.sc-iBzEeX .ghCdOs.sc-lbVvki > .sc-hmbstg.xvsQk")
    SIGN_IN_BUTTON_FORM = (By.CSS_SELECTOR, ".cdTyhF.dSzotL.jdiWPe.sc-bBjRSN.sc-eirqVv.sc-iNiQyp")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")

class BasePage:
    """Contains driver init. and basic methods for all pages.
       Timeout can be changed. 10 secs is default number."""

    def __init__(self, driver: RemoteWebDriver):
        """
        BasePage instance.
        :param driver: WebDriver instance
        :param timeout: implicit wait used by WebDriverWait (default: 30 seconds)
        :return: None
        """
        self.driver = driver

    def login(self):
        self.open(Urls.MAIN_URL)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]").click()
        self.find_element_and_click(*LoginPageLocators.SIGN_IN_BUTTON_HEADER)
        self.find_element_and_send_keys(*LoginPageLocators.EMAIL_INPUT, Const.EMAIL)
        self.find_element_and_send_keys(*LoginPageLocators.PASSWORD_INPUT, Const.PASSWORD)
        self.find_element_and_click(*LoginPageLocators.SIGN_IN_BUTTON_FORM)
        time.sleep(4)

    def is_element_present(self, method: str, value: str) -> bool:
        """Return True, if element is presented on the screen. Otherwise - False"""
        try:
            self.driver.find_element(method, value)
        except NoSuchElementException:
            return False
        return True

    def navigate(self, page_name):
        """Opens given link."""
        self.driver.get(Urls.MAIN_URL + page_name)

    def find_element_and_send_keys(self, method: str, value: str, text: str):
        """Find element by method and value, than send given keys."""
        return self.driver.find_element(method, value).send_keys(text)

    def find_element_and_click(self, method: str, value: str):
        """Find element by method and value, than click on it."""
        return self.driver.find_element(method, value).click()

    def get_element_text(self, method: str, value: str):
        """Find element and return text from it."""
        return self.driver.find_element(method, value).text

    def element_by_visible_text_is_present(self, visible_text, element_type):
        locator = f'//{element_type}[contains(text(), "{visible_text}")]'
        return self.is_element_present(By.XPATH, locator)

    def find_and_click_element_by_visible_text(self, visible_text):
        locator = f'//*[contains(text(), "{visible_text}")]'
        return self.driver.find_element(By.XPATH, locator).click()

    def find_element_by_visible_text(self, visible_text):
        locator = f'//*[contains(text(), "{visible_text}")]'
        return self.driver.find_element(By.XPATH, locator)
