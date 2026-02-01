import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

class TestLogin:
    @pytest.mark.parametrize("username,password,expected_success,expected_error", [
        ("standard_user", "secret_sauce", True, None),  # 1. Успешный логин
        ("standard_user", "wrong_password", False, "Username and password do not match"),  # 2. Неверный пароль
        ("locked_out_user", "secret_sauce", False, "locked out"),  # 3. Заблокированный
        ("", "", False, "Username is required"),  # 4. Пустые поля
        ("performance_glitch_user", "secret_sauce", True, None),  # 5. Performance glitch
    ])
    def test_login_scenarios(self, driver, username, password, expected_success, expected_error):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)
        
        if expected_success:
            assert login_page.is_inventory_page_loaded(), "Не удалось зайти в систему"
        else:
            error_text = login_page.get_error_message().lower()
            assert expected_error.lower() in error_text, f"Ожидалось '{expected_error}', но получили: '{error_text}'"
