import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from settings import Urls, Const


class ProjectPageLocators:
    USERS_BUTTON = ""
    ACTIVE_SESSIONS_BUTTON = ""
    NETWORK_BUTTON = ""
    SETTINGS_BUTTON = ""
    EXPORT_DATA_BUTTON = ""
    LOG_BUTTON = ""
    BILLING_BUTTON = ""
    UPLOAD_IMAGE_BUTTON = (By.CSS_SELECTOR, "input#settingsButtonUploadImage")


class PangoJuneProjectPage(BasePage):

    def assert_active_sessions_by_protocol_chart(self):
        self.navigate(Urls.PANGO_JUNE_03_DASHBOARD)
        return self.element_by_visible_text_is_present("hydra-tcp", "div")

    def open_users_tab(self):
        self.navigate(Urls.PANGO_JUNE_03_USERS)

    def users_search_field_displayed(self):
        return self.element_by_visible_text_is_present("Search users", "div")

    def open_countries_tab(self):
        self.navigate(Urls.PANGO_JUNE_03_COUNTRIES)

    def verify_countries_screen_displayed(self):
        self.open_countries_tab()
        return self.element_by_visible_text_is_present("Add location", "div")

    def open_locations_tab(self):
        self.navigate(Urls.PANGO_JUNE_03_LOCATIONS)

    def verify_locations_displayed(self):
        self.open_locations_tab()
        return self.element_by_visible_text_is_present("Server pools for", "div")

    def open_pools_tab(self):
        self.navigate(Urls.PANGO_JUNE_03_POOLS)

    def verify_pools_displayed(self):
        self.open_pools_tab()
        return self.element_by_visible_text_is_present("SomeTech", "div")

    def open_settings_tab(self):
        self.navigate(Urls.PANGO_JUNE_03_SETTINGS)

    def verify_project_description_displayed(self):
        self.open_settings_tab()
        return self.element_by_visible_text_is_present(Const.PANGO_JUNE_03_DESCRIPTION_TEXT, "textarea")

    def verify_upload_image_button_displayed(self):
        return self.is_element_present(*ProjectPageLocators.UPLOAD_IMAGE_BUTTON)

    def open_billing_page(self):
        self.navigate(Urls.PANGO_JUNE_03_BILLING)

    def verify_billing_page_displayed(self):
        self.open_billing_page()
        self.find_and_click_element_by_visible_text("Show features")
        return self.element_by_visible_text_is_present("User management", "div")