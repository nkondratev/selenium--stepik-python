import time
from selenium.webdriver.common.by import By

URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_can_see_add_to_basket_button(browser):
    browser.get(URL)
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена на странице"
