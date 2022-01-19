from pages.user_tab import UserTab


def test_verify_change_traffic_scenario(driver):
    page = UserTab(driver)
    result = page.verify_change_user_traffic_scenario()
    assert result is True


def test_verify_user_not_deleted_if_id_is_not_correct(driver):
    page = UserTab(driver)
    result = page.delete_user_data("714167437", "pango_july15", "12345678")
    assert result is False
