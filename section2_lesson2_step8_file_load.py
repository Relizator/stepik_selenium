from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поля с именем, фамилией и email
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("ivan@petrov.ru")

    # Выбираем файл для загрузки, расположенный в директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))  
    file_path = os.path.join(current_dir, 'test.txt')
    input4 = browser.find_element(By.NAME, "file")
    input4.send_keys(file_path)

    # Нажимаем на кнопку для отправки данных
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
