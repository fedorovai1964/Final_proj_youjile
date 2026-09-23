import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.ConfigProvider import ConfigProvider


class AuthPage():

    def __init__(self, driver: WebDriver) -> None:

        self.__url = ConfigProvider().get_ui_url()
        self.__driver = driver
        self.locators = {
            "email": "[placeholder='example@mail.ru']",
            "password": "[autocomplete='current-password']",
            "sign_in": "div[role='button']",
            "main_page": "//div[@class='text-sm-semibold"
                         " text-panel-text-primary cursor-default']"
        }

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под  {email}:{password}")
    def login_as(self, email: str, password: str):
        # ожидаем появления поля логина
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, self.locators["email"]),))
        your_email = self.__driver.find_element(
            By.CSS_SELECTOR, self.locators["email"])
        your_email.clear()
        your_email.send_keys(email)

        your_pass = self.__driver.find_element(
            By.CSS_SELECTOR, self.locators["password"])
        your_pass.clear()
        your_pass.send_keys(password)

        self.__driver.find_element(
            By.CSS_SELECTOR, self.locators['sign_in']).click()

        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, self.locators["main_page"])))


    @allure.step("Убедиться, что главная страница загружена:есть'My company'")
    def сompany_search(self):
        search_title = self.__driver.find_element(
            By.XPATH, self.locators["main_page"]).text
        return search_title
