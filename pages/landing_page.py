"""This module contains Landing page interaction methods (Page object)."""
import time
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.common.by import By
from settings import Const
from pages.base_page import LoginPageLocators


class LandingPage(BasePage):

    def verify_forgot_password_screen_opened(self):
        self.find_and_click_element_by_visible_text(Const.EMAIL)
        self.find_and_click_element_by_visible_text("Logout")
        self.driver.find_element_by_css_selector("button[role='button'] > span").click()
        self.find_and_click_element_by_visible_text("Forgot password?")
        return self.element_by_visible_text_is_present("Forgotten password", "div")
