# Тестирование авторизации saucedemo.com

## Требования
- Python 3.10
- Chrome/Chromedriver

## Установка и запуск

### Локальный запуск:
1. Создать виртуальное окружение: `python -m venv venv`
2. Активировать: `venv\Scripts\activate` (Windows) или `source venv/bin/activate` (Mac/Linux)
3. Установить зависимости: `pip install -r requirements.txt`
4. Запустить тесты: `pytest tests/ -v`

### Запуск с Allure отчетами:
1. `pytest tests/ --alluredir=allure-results`
2. `allure serve allure-results`

### Запуск в Docker:
1. Собрать образ: `docker build -t saucedemo-tests .`
2. Запустить: `docker run saucedemo-tests`

## Структура проекта
- `tests/test_login.py` - 5 тестов авторизации
- `pages/login_page.py` - Page Object для страницы логина
- `conftest.py` - фикстура WebDriver
- `Dockerfile` - конфигурация для Docker
- `requirements.txt` - зависимости
