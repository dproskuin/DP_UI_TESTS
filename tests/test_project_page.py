"""Tests related to Projects"""
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
    result = page.verify_active_sessions_by_protocol_chart()
    assert result is True


def test_countries_page_displayed(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_countries_screen_displayed()
    assert result is True


def test_billing_page_displayed(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_billing_page_displayed()
    assert result is True


def test_verify_user_is_owner(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_user_is_owner()
    assert result is True


def test_verify_user_email_displayed(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_user_email_displayed()
    assert result is True


def test_verify_project_search(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_project_search_result_displayed("pango_june03")
    assert result is True


def test_verify_add_project_button_navigation(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_add_project_button_navigation()
    assert driver.current_url == "https://developer.anchorfree.com/createProject"
    assert result is True


def test_verify_ability_to_add_and_delete_country(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_ability_to_add_and_delete_country()
    assert result is True


def test_verify_user_search_options(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_user_search_options()
    assert result is True


def test_verify_ability_to_change_projects_view_to_list(driver):
    page = PangoJuneProjectPage(driver)
    result = page.verify_ability_to_change_projects_view_to_list()
    assert result is True

