import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

class TestLogin:
    @pytest.mark.parametrize("username,password,expected,error_contains", [
        ("standard_user", "secret_sauce", True, None),
        ("standard_user", "wrong_password", False, "do not match"),
        ("locked_out_user", "secret_sauce", False, "locked out"),
        ("", "", False, "Username is required"),
        ("performance_glitch_user", "secret_sauce", True, None),
    ])
    def test_login_scenarios(self, driver, username, password, expected, error_contains):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)
        
        if expected:
            assert login_page.is_inventory_page_loaded(), "Не удалось зайти в систему"
        else:
            error_text = login_page.get_error_message().lower()
            assert error_contains.lower() in error_text, f"Ожидалось '{error_contains}', но получили: '{error_text}'"