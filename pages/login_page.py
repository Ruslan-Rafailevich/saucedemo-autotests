from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        
    def open(self):
        self.driver.get(self.url)
        
    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        
    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        
    def is_inventory_page_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/inventory.html")
            )
            return True
        except:
            return False