"""This module describes Base page interaction methods (Page object)."""
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import settings
from settings import Const, Urls


class LoginPageLocators:
    SIGN_IN_BUTTON_HEADER = (By.CSS_SELECTOR, "button#react-collapsed-toggle-1")
    SIGN_IN_BUTTON_FORM = (By.CSS_SELECTOR, "[data-test-id='button.signin']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")


class BasePage:

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver

    def login(self, email: str, password: str):
        """
        Navigate to Landing page and login into account.
        If wrong password error appeared, use another password - In order to avoid errors with "change password" tests.
        :param email: string, user emal
        :param password: string, user password
        :return: None
        """
        self.navigate('')
        self.find_element_and_send_keys(*LoginPageLocators.EMAIL_INPUT, email)
        self.find_element_and_send_keys(*LoginPageLocators.PASSWORD_INPUT, password)
        self.find_element_and_click(*LoginPageLocators.SIGN_IN_BUTTON_FORM)

        if self.element_by_visible_text_is_present("Email and password do not match", "div"):
            self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Keys.CONTROL + 'a' + Keys.BACK_SPACE)
            self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).clear()
            self.find_element_and_send_keys(*LoginPageLocators.PASSWORD_INPUT, settings.Const.NEW_PASSWORD)
            self.find_element_and_click(*LoginPageLocators.SIGN_IN_BUTTON_FORM)
        time.sleep(4)

    def raw_login(self, email, password):
        self.navigate('')
        self.find_element_and_send_keys(*LoginPageLocators.EMAIL_INPUT, email)
        self.find_element_and_send_keys(*LoginPageLocators.PASSWORD_INPUT, password)
        self.find_element_and_click(*LoginPageLocators.SIGN_IN_BUTTON_FORM)
        time.sleep(4)

    def is_element_present(self, method: str, value: str) -> bool:
        """Return True, if element is presented on the screen. Otherwise - False"""
        try:
            self.driver.find_element(method, value)
        except NoSuchElementException:
            print(f'Element {value} not found!')
            return False
        return True

    def navigate(self, page_name):
        """Opens given URL."""
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

    def element_by_visible_text_is_present(self, visible_text: str, element_type: str):
        locator = f'//{element_type}[contains(text(), "{visible_text}")]'
        return self.is_element_present(By.XPATH, locator)

    def find_and_click_element_by_visible_text(self, visible_text):
        locator = f'//*[contains(text(), "{visible_text}")]'
        return self.driver.find_element(By.XPATH, locator).click()

    def find_element_by_visible_text(self, visible_text):
        locator = (By.XPATH, f'//*[contains(text(), "{visible_text}")]')
        return self.driver.find_element(*locator)

    def find_and_click_button_by_text(self, visible_text):
        locator = f"//button[text()='{visible_text}']"
        return self.driver.find_element(By.XPATH, locator).click()

    def logout(self):
        """Logout via user's panel."""
        self.find_and_click_element_by_visible_text(Const.EMAIL)
        self.find_and_click_element_by_visible_text("Logout")
