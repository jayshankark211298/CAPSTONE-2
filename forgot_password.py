from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrangeHRMTest:
    def __init__(self):
        # Initialize the WebDriver
        chromedriver_path = r'C:\Users\User\Desktop\workspace\PAT-25\Jay_selenium\chromedriver.exe'  # Replace with your actual path
        self.driver = webdriver.Chrome(service=Service(chromedriver_path))
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait with a 10-second timeout

    def visit_site(self, url):
        # Visit the provided URL
        self.driver.get(url)
        # Validate that the page has loaded by checking the URL
        assert self.driver.current_url == url, f"Failed to load the site. Expected URL: {url}, but got {self.driver.current_url}"
        print("Site loaded successfully.")

    def click_forgot_password(self):
        # Wait for the 'Forgot your password?' link to be clickable and then click it
        forgot_password_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")))
        assert forgot_password_link.is_displayed(), "'Forgot your password?' link is not displayed."
        forgot_password_link.click()
        print("'Forgot your password?' link clicked successfully.")
        # Validate that the Forgot Password page loaded
        assert self.driver.current_url.endswith("/requestPasswordResetCode"), "Failed to navigate to the Forgot Password page."
        print("Navigated to the Forgot Password page successfully.")

    def reset_password(self, username):
        # Wait for the username input field, enter the username, and click the reset button
        username_field = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-input")))
        assert username_field.is_displayed(), "Username input field is not displayed."
        username_field.send_keys(username)
        print(f"Username '{username}' entered successfully.")

        reset_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        assert reset_button.is_displayed(), "Reset button is not displayed."
        reset_button.click()
        print("Reset button clicked successfully.")
        # Validate that the reset process started (you might need to check for a success message or page change)
        success_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "orangehrm-card-container")))
        assert success_message.is_displayed(), "Password reset process did not start."
        print("Password reset process initiated successfully.")

    def close_browser(self):
        # Close the browser window
        self.driver.quit()
        print("Browser closed successfully.")


# Usage
if __name__ == "__main__":
    test = OrangeHRMTest()
    test.visit_site("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    test.click_forgot_password()
    test.reset_password("Admin")
    test.close_browser()
