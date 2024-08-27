import pytest
from forgot_password import OrangeHRMTest
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def orangehrm_test():
    test_instance = OrangeHRMTest()
    yield test_instance
    test_instance.close_browser()


def test_visit_site(orangehrm_test):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    orangehrm_test.visit_site(url)
    assert orangehrm_test.driver.current_url == url, f"Failed to load the site. Expected URL: {url}, but got {orangehrm_test.driver.current_url}"


def test_click_forgot_password(orangehrm_test):
    orangehrm_test.click_forgot_password()
    assert orangehrm_test.driver.current_url.endswith(
        "/requestPasswordResetCode"), "Failed to navigate to the Forgot Password page."


def test_reset_password(orangehrm_test):
    username = "Admin"
    orangehrm_test.reset_password(username)

    # Corrected way to find the element using By.CLASS_NAME
    success_message = orangehrm_test.wait.until(
        lambda driver: driver.find_element(By.CLASS_NAME, "orangehrm-card-container")
    )

    assert success_message.is_displayed(), "Password reset process did not start."