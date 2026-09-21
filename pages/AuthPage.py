import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage():

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://ru.yougile.com/team/"
        self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под  {email}:{password}")
    def login_as(self, email: str, password: str):
        # ожидаем появления поля логина
        (WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='example@mail.ru']"))))
        your_email = self.__driver.find_element(By.CSS_SELECTOR, "[placeholder='example@mail.ru']")
        your_email.clear()
        your_email.send_keys(email)


        your_pass = self.__driver.find_element(By.CSS_SELECTOR, "[autocomplete='current-password']")
        your_pass.clear()
        your_pass.send_keys(password)

        (self.__driver.find_element(By.CSS_SELECTOR, "div[role='button']").click())

        #Ожидаем появления логотипа(убеждаемся что главная страница полностью загружена)
        (WebDriverWait(self.__driver, 10).until((EC.visibility_of_element_located((By.XPATH, "//div[@class='text-sm-semibold text-panel-text-primary cursor-default']")))))

    @allure.step("Убедиться, что загружена главная страница по наличию строки 'My company'")
    def сompany_search(self):
        search_title = self.__driver.find_element(By.XPATH, "//div[@class='text-sm-semibold text-panel-text-primary cursor-default']").text
        return search_title



