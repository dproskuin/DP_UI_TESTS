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


def test_verify_country_list_options(driver):
    page = UserProfilePage(driver)
    result = page.verify_country_list_options()
    assert result is True





