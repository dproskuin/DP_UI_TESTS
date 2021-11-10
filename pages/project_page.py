from pages.base_page import BasePage
from settings import Urls


class ProjectPageLocators:
    USERS_BUTTON = ""
    ACTIVE_SESSIONS_BUTTON = ""
    NETWORK_BUTTON = ""
    SETTINGS_BUTTON = ""
    EXPORT_DATA_BUTTON = ""
    LOG_BUTTON = ""
    BILLING_BUTTON = ""


class ProjectPage(BasePage):

    def open_users_tab(self):
        self.navigate(Urls.PANGO_JUNE_03_USERS)

    def users_search_field_displayed(self):
        return self.element_by_visible_text_is_present("Search users", "div")
