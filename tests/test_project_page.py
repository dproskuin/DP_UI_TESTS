from pages.project_page import PangoJuneProjectPage


def test_search_users_field_displayed(driver):
    page = PangoJuneProjectPage(driver)
    page.open_users_tab()
    result = page.users_search_field_displayed()
    assert result is True


def test_pools_displayed(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_pools_displayed()
    assert result is True


def test_settings_page_displayed(driver):
    page = PangoJuneProjectPage(driver)
    page.open_settings_tab()
    button_result = page.verify_upload_image_button_displayed()
    description_result = page.verify_project_description_displayed()
    assert button_result and description_result is True


def test_locations_page_displayed(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_locations_displayed()
    assert result is True


def test_active_sessions_chart_displayed(driver):
    page = PangoJuneProjectPage(driver)
    result = page.assert_active_sessions_by_protocol_chart()
    assert result is True


def test_countries_page_displayed(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_countries_screen_displayed()
    assert result is True


def test_billing_page_displayed(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_billing_page_displayed()
    assert result is True
