from pages.landing_page import LandingPage


def test_forgot_password_screen(driver):
    page = LandingPage(driver)
    result = page.verify_forgot_password_screen_opened()
    assert result is True
