import allure
import pytest
import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class TestLogin:
    @allure.title("Успешный логин (standard_user)")
    @allure.description("Проверка успешной авторизации с корректными данными")
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        
        with allure.step("Вводим логин и пароль standard_user"):
            login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Проверяем переход на страницу инвентаря"):
            assert "/inventory.html" in driver.current_url, \
                f"Ожидался переход на /inventory.html, но текущий URL: {driver.current_url}"
        
        with allure.step("Проверяем наличие контейнера с товарами"):
            inventory_container = driver.find_element(By.ID, "inventory_container")
            assert inventory_container.is_displayed()

    @allure.title("Логин с неверным паролем")
    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        
        with allure.step("Вводим верный логин и неверный пароль"):
            login_page.login("standard_user", "wrong_password")
        
        with allure.step("Проверяем сообщение об ошибке"):
            error_text = login_page.get_error_message()
            assert "Username and password do not match" in error_text, \
                f"Неверное сообщение об ошибке: {error_text}"
        
        with allure.step("Проверяем, что остались на странице логина"):
            assert "saucedemo.com" in driver.current_url

    @allure.title("Логин заблокированного пользователя")
    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        
        with allure.step("Пытаемся войти как locked_out_user"):
            login_page.login("locked_out_user", "secret_sauce")
        
        with allure.step("Проверяем сообщение о блокировке"):
            error_text = login_page.get_error_message()
            assert "locked out" in error_text.lower(), \
                f"Не найдено сообщение о блокировке: {error_text}"
    
    @allure.title("Логин с пустыми полями")
    def test_empty_fields(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        
        with allure.step("Пытаемся войти с пустыми полями"):
            login_page.login("", "")
        
        with allure.step("Проверяем сообщение об ошибке"):
            error_text = login_page.get_error_message()
            assert "Username is required" in error_text, \
                f"Неверное сообщение об ошибке: {error_text}"

    @allure.title("Логин пользователем performance_glitch_user")
    def test_performance_glitch_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        
        with allure.step("Засекаем время входа"):
            start_time = time.time()
            login_page.login("performance_glitch_user", "secret_sauce")
            end_time = time.time()
            login_time = end_time - start_time
        
        with allure.step("Проверяем что вход выполнен несмотря на задержки"):
            assert "/inventory.html" in driver.current_url, \
                f"Ожидался переход на /inventory.html, но текущий URL: {driver.current_url}"
            
            allure.attach(
                f"Время входа: {login_time:.2f} секунд",
                name="Login time",
                attachment_type=allure.attachment_type.TEXT
            )
            
            print(f"Время входа: {login_time:.2f} секунд")
