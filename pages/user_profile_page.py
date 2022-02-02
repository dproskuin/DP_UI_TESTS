import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from settings import Const, Variables


class UserProfilePageLocators:
    CURRENT_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='currentPwd']")
    NEW_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='newPwd']")
    REPEAT_NEW_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='rePwd']")


class UserProfilePage(BasePage):
    """
    Methods for interacting with User profile and verify-methods for elements.
    """

    def open_profile(self):
        self.open_user_dropdown()
        self.find_and_click_element_by_visible_text(Variables.VIEW_PROFILE_BUTTON)

    def open_user_dropdown(self):
        if self.element_by_visible_text_is_present(Const.EMAIL, 'div') is False:
            time.sleep(3)
        self.find_and_click_element_by_visible_text(Const.EMAIL)

    def verify_switch_between_profile_tabs(self):
        self.open_profile()
        self.find_and_click_element_by_visible_text(Variables.ACCOUNT_SECURITY_TAB_BUTTON)
        return self.element_by_visible_text_is_present(Variables.TWO_FACTOR_AUTH, "div")

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

    def verify_ability_to_logout(self):
        self.logout()
        return self.element_by_visible_text_is_present(Variables.SIGN_IN_BUTTON, "div")

    def change_password(self, new_password, current_password):
        self.open_profile()
        self.find_and_click_element_by_visible_text(Variables.ACCOUNT_SECURITY_TAB_BUTTON)
        self.find_element_and_send_keys(*UserProfilePageLocators.CURRENT_PASSWORD_FIELD, current_password)
        self.find_element_and_send_keys(*UserProfilePageLocators.NEW_PASSWORD_FIELD, new_password)
        self.find_element_and_send_keys(*UserProfilePageLocators.REPEAT_NEW_PASSWORD_FIELD, new_password)
        time.sleep(2)
        element = self.find_element_by_visible_text(Variables.CHANGE_PASSWORD_BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.find_and_click_button_by_text(Variables.CHANGE_PASSWORD_BUTTON)
        time.sleep(2.5)

    def verify_ability_to_change_password(self):
        """ This method uses "change password" method. Scenario:
            1. Change password from PASSWORD to NEW_PASSWORD
            2. Logout and go to login screen
            3. Login
            4. Change password back from NEW to PASSWORD
        """
        self.change_password(Const.NEW_PASSWORD, Const.PASSWORD)
        time.sleep(4)
        self.logout()
        self.navigate("")
        self.login(Const.EMAIL, Const.NEW_PASSWORD)
        self.change_password(Const.PASSWORD, Const.NEW_PASSWORD)
        return self.element_by_visible_text_is_present(Variables.PASSWORD_CHANGED_SUCCESS, "div")

    def verify_error_when_current_password_is_not_correct(self):
        """ Verify error displayed when user entered wrong password in to "current password" field. """
        self.change_password("111111111111", "222222222222")
        return self.element_by_visible_text_is_present(Variables.ENTER_CURRENT_PASSWORD_MESSAGE, "div")

    def open_country_list(self):
        return self.driver.find_element(By.NAME, "country").click()

    def verify_country_list(self):
        """ Go to User profile and assert countries list opened and contains "UAE" option. """
        self.open_profile()
        self.open_country_list()
        return self.element_by_visible_text_is_present(Variables.UAE, "option")

    def verify_email_unavailable_to_edit(self):
        self.open_profile()
        element = self.driver.find_element_by_css_selector("input[name='email']")
        return element.is_enabled()
