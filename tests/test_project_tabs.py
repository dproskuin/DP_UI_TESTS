from pages.project_page import ProjectPage


def test_users_tab_opened(driver):
    page = ProjectPage(driver)
    page.login()
    page.open_users_tab()
    result = page.users_search_field_displayed()
    assert result == True
