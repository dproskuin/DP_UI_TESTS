import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    PROJECT_SEARCH_BUTTON = (By.CSS_SELECTOR, "div#ICON_PROJECT_SEARCH > .label")
    PROJECT_SEARCH_INPUT = (By.CSS_SELECTOR, "input#inputDefaultId1")
    DE_LOCATION_DELETE_BUTTON = (By.XPATH, "//*[@id='screenNetwork']/table/tbody/tr[1]/td[4]")
    USERS_SEARCH_BUTTON = (By.CSS_SELECTOR, ".blue.flex.icons.iconsStyle1.search > svg > path")
    USERS_FILTER_BUTTON = (By.CSS_SELECTOR, ".filterButton")
    USER_SEARCH_OPTIONS = ["User ID", "User Name", "User Token", "Device ID"]


class PangoJuneProjectPage(BasePage):

    def verify_active_sessions_by_protocol_chart(self):
        self.navigate(Urls.PANGO_JUNE_03_DASHBOARD)
        return self.element_by_visible_text_is_present("hydra-tcp", "div")

    def open_users_tab(self):
        self.navigate(Urls.PANGO_JUNE_03_USERS)

    def verify_delete_user_screen_opened(self):
        pass

    def verify_user_not_deleted_if_id_is_incorrect(self):
        pass

    def verify_user_search_options(self):
        self.open_users_tab()
        self.find_element_and_click(*ProjectPageLocators.USERS_SEARCH_BUTTON)
        self.find_element_and_click(*ProjectPageLocators.USERS_FILTER_BUTTON)

        for option in ProjectPageLocators.USER_SEARCH_OPTIONS:

            if self.find_element_by_visible_text(option):
                return True
            return False

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
        time.sleep(5)
        self.find_element_by_visible_text("Show features").click()
        return self.element_by_visible_text_is_present("User management", "div")

    def verify_user_is_owner(self):
        self.navigate(Urls.PANGO_JUNE_03_DASHBOARD)
        return self.element_by_visible_text_is_present("OWNER", "div")

    def verify_user_email_displayed(self):
        return self.element_by_visible_text_is_present(Const.EMAIL, "span")

    def search_the_project(self, project_name):
        self.find_element_and_click(*ProjectPageLocators.PROJECT_SEARCH_BUTTON)
        self.find_element_and_send_keys(*ProjectPageLocators.PROJECT_SEARCH_INPUT, project_name)

    def verify_project_search_result_displayed(self, project_name):
        self.search_the_project("june03")
        return self.element_by_visible_text_is_present(project_name, "div")

    def verify_add_project_button_navigation(self):
        self.find_and_click_element_by_visible_text("Add project")
        return self.element_by_visible_text_is_present("Create project", "h1")

    def verify_ability_to_add_and_delete_country(self):
        self.open_countries_tab()
        if self.element_by_visible_text_is_present("Germany", "div") is True:
            add_button = self.find_element_by_visible_text("Add location")
            self.driver.find_element(*ProjectPageLocators.DE_LOCATION_DELETE_BUTTON).click()
            time.sleep(1)
            add_button.click()
            select = Select(self.driver.find_element_by_css_selector("select"))
            select.select_by_index(0)
            return self.element_by_visible_text_is_present("Germany", "div")
