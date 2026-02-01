# Автотесты для сайта saucedemo.com

## Техническое задание
Автоматизировать тестирование логина на сайте https://www.saucedemo.com/ с использованием Python.
5 тестов, проверяющих разные сценарии авторизации.

## Требования
- Python 3.10
- Chrome/Chromedriver

## Структура проекта
- `tests/test_login.py` – 5 тестов авторизации
- `pages/login_page.py` – Page Object для страницы логина
- `conftest.py` – настройка WebDriver и Allure
- `Dockerfile` – конфигурация для Docker
- `requirements.txt` – зависимости

## Запуск тестов

### Локальный запуск:
1. Создать виртуальное окружение: `python -m venv venv`
2. Активировать: `venv\Scripts\activate` (Windows) или `source venv/bin/activate` (Mac/Linux)
3. Установить зависимости: `pip install -r requirements.txt`
4. Запустить тесты: `pytest tests/ -v`

### Запуск с Allure отчетом:
1. Запустить тесты с генерацией результатов: `pytest tests/ --alluredir=allure-results -v`
2. Просмотреть отчет: `allure serve allure-results`
3. Или сгенерировать HTML отчет: `allure generate allure-results -o allure-report --clean`

### Запуск в Docker:
1. Собрать образ: `docker build -t saucedemo-tests .`
2. Запустить тесты: `docker run --rm -v ${PWD}/allure-results:/app/allure-results saucedemo-tests`
3. Просмотреть отчет: `allure serve allure-results`

### Сценарии тестирования:
1. Успешный логин (standard_user / secret_sauce)
2. Логин с неверным паролем
3. Логин заблокированного пользователя (locked_out_user)
4. Логин с пустыми полями
5. Логин пользователем performance_glitch_user

## Используемые технологии
- Python 3.10
- Selenium WebDriver
- Pytest
- Allure Framework
- Docker
- Page Object Pattern
