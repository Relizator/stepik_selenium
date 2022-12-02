from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля: First name, Last name, Email
    input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
    input3.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждём загрузки страницы, чтобы проверить, что смогли зарегистрироваться
    time.sleep(1)

    # Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ожидание, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
