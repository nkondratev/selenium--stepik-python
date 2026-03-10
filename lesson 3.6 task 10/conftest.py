import pytest
from selenium import webdriver

from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Choose language for browser"
    )


@pytest.fixture
def browser(request):
    # Если ваш драйвер не лежит по стандартному пути то следует удалить # и указать свой путь, а webdriver.Firefox надо писать webdriver.Firefox(options=options, service=service), и тоже самое в Chrome()
    # service = Service("/snap/bin/geckodriver")
    language = request.config.getoption("--language")
    # Если у вас Chrome, то замените уберите знак # со всех следующих строк и уберите все строки ниже кроме yield driver и driver.quit()
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # driver = webdriver.Chrome(options=options)
    options = webdriver.FirefoxOptions()
    options.set_preference("intl.accept_languages", language)
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
