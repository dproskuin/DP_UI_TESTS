from pages.user_tab import UserTab


def test_verify_change_traffic_scenario(driver):
    page = UserTab(driver)
    result = page.verify_change_traffic_scenario()
    assert result is True
