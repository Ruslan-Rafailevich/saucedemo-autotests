from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

print("=== ТЕСТ CHROMEDRIVER ===")

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


try:
    print("1. Устанавливаем ChromeDriver...")
    service = Service(ChromeDriverManager().install())
    
    print("2. Создаем драйвер...")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    print("3. Открываем сайт...")
    driver.get("https://www.saucedemo.com")
    
    print(f"✅ УСПЕХ! Заголовок: {driver.title}")
    print(f"✅ URL: {driver.current_url}")
    
    # Проверяем элементы
    from selenium.webdriver.common.by import By
    elements = driver.find_elements(By.ID, "user-name")
    print(f"✅ Найдено элементов на странице: {len(elements)}")
    
    driver.quit()
    print("✅ Драйвер закрыт")
    
except Exception as e:
    print(f"❌ ОШИБКА: {e}")
    import traceback
    traceback.print_exc()
