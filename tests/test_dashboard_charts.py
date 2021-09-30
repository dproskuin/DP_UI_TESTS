from pages.dashboard_page import DashboardPage
from settings import Urls

def test_active_sessions_chart(driver):
    page = DashboardPage(driver)
    page.login()
    page.navigate(Urls.PANGO_JUNE_03_DASHBOARD)
    assert page.assert_active_sessions_by_protocol_chart() is True
