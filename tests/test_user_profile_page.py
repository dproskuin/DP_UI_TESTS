"""Tests related to User"""
from pages.user_profile_page import UserProfilePage


def test_verify_switch_between_profile_tabs(driver):
    page = UserProfilePage(driver)
    result = page.verify_switch_between_profile_tabs()
    assert result is True


def test_verify_user_dropdown_options(driver):
    page = UserProfilePage(driver)
    result = page.verify_user_dropdown_list_options()
    assert result is True


def test_verify_ability_to_logout(driver):
    page = UserProfilePage(driver)
    result = page.verify_ability_to_logout()
    assert result is True


def test_verify_ability_to_change_password(driver):
    page = UserProfilePage(driver)
    result = page.verify_ability_to_change_password()
    assert result is True


def test_verify_country_list(driver):
    page = UserProfilePage(driver)
    result = page.verify_country_list()
    assert result is True


def test_verify_email_unavailable_to_edit(driver):
    page = UserProfilePage(driver)
    result = page.verify_email_unavailable_to_edit()
    assert result is False


def test_verify_error_when_current_password_is_not_correct(driver):
    page = UserProfilePage(driver)
    result = page.verify_error_when_current_password_is_not_correct()
    assert result is True

