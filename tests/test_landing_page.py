import time

from pages.landing_page import LandingPage
from settings import Const


def test_forgot_password_screen(driver):
    page = LandingPage(driver)
    result = page.verify_forgot_password_screen_opened()
    assert result is True


def test_error_displayed_when_login_with_wrong_email(driver):
    page = LandingPage(driver)
    page.logout()
    page.login("abcd@test.com", Const.PASSWORD)
    result = page.verify_error_when_login_with_wrong_email()
    assert result is True


def test_error_displayed_when_login_with_wrong_password(driver):
    page = LandingPage(driver)
    page.logout()
    page.login(Const.EMAIL, "123")
    result = page.verify_error_when_login_with_wrong_password()
    assert result is True


def test_developer_documentation_page_opened(driver):
    page = LandingPage(driver)
    page.logout()
    link = page.verify_developer_documentation_page_available()
    assert link == "https://auravpn.gitbook.io/paas/"


def test_privacy_policy_page_opened(driver):
    page = LandingPage(driver)
    page.logout()
    link = page.verify_privacy_policy_page_available()
    assert link == "https://www.aura.com/legal/privacy-policy"


def test_tof_page_opened(driver):
    page = LandingPage(driver)
    page.logout()
    link = page.verify_terms_of_service_page_available()
    assert link == "https://www.aura.com/legal"
