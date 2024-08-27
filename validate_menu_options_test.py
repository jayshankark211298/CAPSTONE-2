import pytest
from validate_menu_options import ShankarHeadlessBrowsing

@pytest.fixture(scope="module")
def browser():
    test_instance = ShankarHeadlessBrowsing("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield test_instance
    test_instance.shutdown()

def test_home_page(browser):
    assert browser.home_page(), "Failed to access the home page."

def test_validate_username_input_box(browser):
    assert browser.validate_username_input_box(), "Username input box not found or not enabled."

def test_login(browser):
    assert browser.login(), "Login failed."

def test_navigate_to_admin_page(browser):
    assert browser.navigate_to_admin_page(), "Failed to navigate to the Admin page."

def test_validate_page_title(browser):
    assert browser.validate_page_title(), "Page title validation failed."

def test_validate_admin_page_options(browser):
    assert browser.validate_admin_page_options(), "Admin page options validation failed."
