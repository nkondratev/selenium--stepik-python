from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    # Убери строчку ниже с service если драйвер находится по стандартному пути или замени на свой путь.
    service = Service("/snap/bin/geckodriver")
    # Если установлен Chrome, то замени Firefox(service=service) на Chrome(services=service)
    browser = webdriver.Firefox(service=service)

    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Никто")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Никакой")

    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Moscow")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
