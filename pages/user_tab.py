from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from settings import Urls, Const


class UserTabLocators:
    TRAFFIC_SETTINGS_BUTTON = (By.CSS_SELECTOR, ".blue.icons.iconsStyle1.settings > svg")
    SET_TRAFFIC_UNLIMITED_CHECKBOX_ON = (By.CSS_SELECTOR, "[id] .blue:nth-of-type(3) .checkboxContainer")
    SET_TRAFFIC_UNLIMITED_CHECKBOX_OFF = (By.CSS_SELECTOR, ".checkboxcontainer.off")
    LIMIT_FIELD = (By.CSS_SELECTOR, "input[name='inputDefaultId64']")  # to change


class UserTab(BasePage):

    def verify_change_traffic_scenario(self):
        self.navigate(Urls.PANGO_JULY_15_TEST_USER)
        self.driver.find_element(*UserTabLocators.TRAFFIC_SETTINGS_BUTTON).click()
        self.driver.find_element(*UserTabLocators.SET_TRAFFIC_UNLIMITED_CHECKBOX_ON).click()
        self.driver.find_element(*UserTabLocators.LIMIT_FIELD).send_keys("100000000")
        self.find_and_click_element_by_visible_text("Set limit")
        self.element_by_visible_text_is_present("95.37 Mb", "div")
        self.driver.find_element(*UserTabLocators.TRAFFIC_SETTINGS_BUTTON).click()
        self.driver.find_element(*UserTabLocators.SET_TRAFFIC_UNLIMITED_CHECKBOX_OFF).click()
        self.find_and_click_element_by_visible_text("Set limit")
        return self.element_by_visible_text_is_present("Unlimited", "div")

    def verify_delete_user_screen_opened(self):
        pass

    def verify_user_not_deleted_if_id_is_incorrect(self):
        pass
