from pages.user_tab import UserTab


def test_verify_change_user_traffic_scenario(driver):
    page = UserTab(driver)
    result = page.verify_change_user_traffic_scenario()
    assert result is True


def test_verify_user_not_deleted_if_id_is_not_correct(driver):
    page = UserTab(driver)
    result = page.delete_user_data("714167437", "pango_july15", "12345678")
    assert result is False


def test_verify_sessions_tab(driver):
    page = UserTab(driver)
    result = page.verify_sessions_tab()
    assert result is True


def test_verify_purchases_tab(driver):
    page = UserTab(driver)
    result = page.verify_purchases_tab()
    assert result is True


def test_verify_devices_tab(driver):
    page = UserTab(driver)
    result = page.verify_devices_tab()
    assert result is True
