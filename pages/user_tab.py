import settings
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from settings import Urls


class UserTabLocators:
    TRAFFIC_SETTINGS_BUTTON = (By.CSS_SELECTOR, ".blue.icons.iconsStyle1.settings > svg")
    SET_TRAFFIC_UNLIMITED_CHECKBOX_ON = (By.CSS_SELECTOR, "[id] .blue:nth-of-type(3) .checkboxContainer")
    SET_TRAFFIC_UNLIMITED_CHECKBOX_OFF = (By.CSS_SELECTOR, ".checkboxcontainer.off")
    USER_SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test-id='users.search']")
    DELETE_USER_BUTTON = (By.CSS_SELECTOR, "[data-test-id='user.delete']")
    DELETE_USER_DATA_BUTTON = (By.CSS_SELECTOR, ".menu .modalContent  .submit")
    ERROR_MESSAGE_WRONG_USER_ID = (By.CSS_SELECTOR, ".errorMessage")
    USER_DELETE_ID_FIELD = (By.XPATH, "//*[contains(@id, 'inputDefaultId')]")
    LIMIT_FIELD = (By.CSS_SELECTOR, "input[name='inputDefaultId64']")  # to change


class UserTab(BasePage):
    """
    Methods for interacting and verifying User tab. (Project -> Users -> User)
    """

    def change_user_traffic(self, project_name: str, user_id: str, traffic_in_bytes: int, is_user_unlimited: bool):
        self.navigate(Urls.get_user_url(project_name, user_id))
        self.find_element_and_click(*UserTabLocators.TRAFFIC_SETTINGS_BUTTON)

        if is_user_unlimited is True:
            self.find_element_and_click(*UserTabLocators.SET_TRAFFIC_UNLIMITED_CHECKBOX_ON)
            self.driver.find_element(*UserTabLocators.LIMIT_FIELD).send_keys(traffic_in_bytes)
            print(f"Set {traffic_in_bytes} kb of traffic for user {user_id}...")

        if is_user_unlimited is False:
            self.find_element_and_click(*UserTabLocators.SET_TRAFFIC_UNLIMITED_CHECKBOX_OFF)
            print(f"Change user {user_id} traffic to unlimited...")

        self.find_and_click_element_by_visible_text("Set limit")

    def verify_change_user_traffic_scenario(self):
        self.change_user_traffic("pango_july15", "714167437", 100000000, True)
        self.change_user_traffic("pango_july15", "714167437", 100000000, False)
        return self.element_by_visible_text_is_present("Unlimited", "div")

    def delete_user_data(self, user_id: str, project_name: str, confirmation_user_id: str) -> bool:
        self.navigate(settings.Urls.get_user_url(project_name, user_id))
        self.find_element_and_click(*UserTabLocators.DELETE_USER_BUTTON)
        self.find_element_and_send_keys(*UserTabLocators.USER_DELETE_ID_FIELD, confirmation_user_id)
        self.find_element_and_click(*UserTabLocators.DELETE_USER_DATA_BUTTON)
        if self.is_element_present(*UserTabLocators.ERROR_MESSAGE_WRONG_USER_ID):
            print(f"CONFIRMATION USER ID: {confirmation_user_id} is not correct. User not deleted.")
            return False
        return True

    def verify_sessions_tab(self):
        self.navigate(Urls.get_user_url("pango_july15", "714167437"))
        self.find_and_click_element_by_visible_text("Sessions")
        return self.element_by_visible_text_is_present("No sessions have been found for the chosen period", "div")

    def verify_devices_tab(self):
        self.navigate(Urls.get_user_url("pango_july15", "714167437"))
        self.find_and_click_element_by_visible_text("Devices")
        return self.element_by_visible_text_is_present("Access token", "div")

    def verify_purchases_tab(self):
        self.navigate(Urls.get_user_url("pango_july15", "714167437"))
        self.find_and_click_element_by_visible_text("Purchases")
        return self.element_by_visible_text_is_present("User has no purchases", "div")