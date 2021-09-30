from pages.base_page import BasePage

class DashboardPageLocators:
    pass

class DashboardPage(BasePage):

    def assert_active_sessions_by_protocol_chart(self):
        return self.element_by_visible_text_is_present("hydra-tcp", "div")
