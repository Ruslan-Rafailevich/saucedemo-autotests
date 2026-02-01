from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def get_error_message(self):
        try:
            error_element = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
            return error_element.text
        except:
            return ""

    def is_error_displayed(self):
        try:
            error_element = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
            return error_element.is_displayed()
        except:
            return False

    def wait_for_inventory_page(self):
        return self.wait.until(
            EC.url_contains("/inventory.html")
        )
