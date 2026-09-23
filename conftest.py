import allure
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config import email
from config import password
from selenium import webdriver

from configuration.ConfigProvider import ConfigProvider
from pages.AuthPage import AuthPage
from api.BoardApi import BoardApi


@pytest.fixture()
def browser():
    """Фикстура для открытия, настройки и закрытия браузера Chrome"""
    with allure.step("Открыть и настроить браузер"):

        timeout = ConfigProvider().getint("ui", "timeout")

        browser_name = ConfigProvider().get("ui", "browser_name")
        if browser_name == "chrome":
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        else:
            browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        browser.implicitly_wait(timeout)
        browser.maximize_window()
    with allure.step("Закрыть браузер"):
        yield browser
        browser.quit()


@pytest.fixture()
def auth(browser):
    """Фикстура для авторизации на сайте YouGile"""
    with allure.step("Авторизоваться"):
        auth_page = AuthPage(browser)
        auth_page.go()
        auth_page.login_as(email, password)


@pytest.fixture
def board():
    """Фикстура для создания новой доски и удаления ее после теста"""
    api = BoardApi()

    with allure.step("Создать рандомное имя доски "):
        name = api.random_board_name()
    with allure.step("Создать доску с именем " + name):
        resp = api.create_board(name)
        id_board = resp['id']
    yield id_board, name
    with allure.step("Удалить созданную доску " + name):
        api.delete_board(id_board)
