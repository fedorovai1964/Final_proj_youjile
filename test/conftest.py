import allure
import pytest
from config import email
from config import password
from selenium import webdriver
from pages.AuthPage import AuthPage
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def browser():

    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.maximize_window()
    with allure.step("Закрыть браузер"):
        yield browser
        browser.quit()

@pytest.fixture()
def auth(browser):
    with allure.step("Авторизоваться"):
        auth_page = AuthPage(browser)
        auth_page.go()
        auth_page.login_as(email, password)