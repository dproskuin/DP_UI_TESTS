import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from settings import Const


class UserProfilePageLocators:
    CURRENT_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='currentPwd']")
    NEW_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='newPwd']")
    REPEAT_NEW_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='rePwd']")


class UserProfilePage(BasePage):

    def open_profile(self):
        self.open_user_dropdown()
        self.find_and_click_element_by_visible_text("View Profile")

    def open_user_dropdown(self):
        self.find_and_click_element_by_visible_text(Const.EMAIL)

    def verify_switch_between_profile_tabs(self):
        self.open_profile()
        self.find_and_click_element_by_visible_text("Account security")
        return self.element_by_visible_text_is_present("Two-factor authentication", "div")

    def verify_user_dropdown_list_options(self):
        self.open_user_dropdown()
        option_1 = self.element_by_visible_text_is_present("View Profile", "div")
        option_2 = self.element_by_visible_text_is_present("Language", "div")
        option_3 = self.element_by_visible_text_is_present("Profile", "div")

        try:

            if option_1 and option_2 and option_3 is True:
                return True

        except NoSuchElementException:

            print("Element is missing!")
            return False

    def logout(self):
        self.open_user_dropdown()
        self.find_and_click_element_by_visible_text("Logout")

    def verify_ability_to_logout(self):
        self.logout()
        return self.element_by_visible_text_is_present("Sign In", "div")

    def change_password(self, new_password, current_password):
        self.open_profile()
        self.find_and_click_element_by_visible_text("Account security")
        self.find_element_and_send_keys(*UserProfilePageLocators.CURRENT_PASSWORD_FIELD, current_password)
        self.find_element_and_send_keys(*UserProfilePageLocators.NEW_PASSWORD_FIELD, new_password)
        self.find_element_and_send_keys(*UserProfilePageLocators.REPEAT_NEW_PASSWORD_FIELD, new_password)
        time.sleep(2)
        self.find_and_click_button_by_text("Change password")
        time.sleep(2.5)

    def verify_ability_to_change_password(self):
        self.change_password(Const.NEW_PASSWORD, Const.PASSWORD)
        time.sleep(4)
        self.navigate("")
        self.login(Const.EMAIL, Const.NEW_PASSWORD)
        self.change_password(Const.PASSWORD, Const.NEW_PASSWORD)
        return self.element_by_visible_text_is_present("Your password has been successfully changed", "div")

    def open_country_list(self):
        return self.driver.find_element(By.NAME, "country").click()

    def verify_country_list_options(self):
        self.open_profile()
        self.open_country_list()
        return self.element_by_visible_text_is_present("United Arab Emirates", "option")
