"""This module contains Landing page interaction methods (Page object)."""
import time

from pages.base_page import BasePage
from settings import Const


class LandingPage(BasePage):

    def verify_forgot_password_screen_opened(self):
        self.find_and_click_element_by_visible_text(Const.EMAIL)
        self.find_and_click_element_by_visible_text("Logout")
        self.find_and_click_element_by_visible_text("Reset password")
        return self.element_by_visible_text_is_present("Forgot password", "div")

    def verify_error_when_login_with_wrong_email(self):
        return self.element_by_visible_text_is_present("Email and password do not match", "div")

    def verify_error_when_login_with_wrong_password(self):
        return self.element_by_visible_text_is_present("Email and password do not match", "div")

    def verify_developer_documentation_page_available(self):
        self.find_and_click_element_by_visible_text("Pango Developer Documentation")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)
        return self.driver.current_url

    def verify_privacy_policy_page_available(self):
        self.find_and_click_element_by_visible_text("Privacy Policy")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)
        return self.driver.current_url

    def verify_terms_of_service_page_available(self):
        self.find_and_click_element_by_visible_text("Terms of Service")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)
        return self.driver.current_url
