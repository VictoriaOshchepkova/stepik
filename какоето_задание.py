from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_registration(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your first name']"
    )
    input1.send_keys("Ivan")

    input2 = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your last name']"
    )
    input2.send_keys("Petrov")

    input3 = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your email']"
    )
    input3.send_keys("test@example.com")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    time.sleep(5)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations" in welcome_text, \
        f"Ожидался текст с Congratulations, получено: {welcome_text}"

    browser.quit()


print("Тест на registration1.html:")
try:
    test_registration("http://suninjuly.github.io/registration1.html")
    print("  Тест прошёл успешно")
except Exception as e:
    print(f"  Тест упал: {type(e).__name__}: {e}")

print("Тест на registration2.html:")
try:
    test_registration("http://suninjuly.github.io/registration2.html")
    print("  Тест прошёл — баг НЕ обнаружен, селекторы не уникальны")
except Exception as e:
    print(f"  Тест упал (баг обнаружен): {type(e).__name__}: {e}")
