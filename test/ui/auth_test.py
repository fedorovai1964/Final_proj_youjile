from config import email
import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def test_auth(browser, auth):
    auth_page = AuthPage(browser)

    with allure.step("Проверить, что страница загружена:есть 'My company'"):
        assert auth_page.сompany_search() == "My company"

    main_page = MainPage(browser)
    main_page.open_menu()

    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL"
                     " заканчивается на../account " + current_url + ""):
        assert current_url.endswith("account")

    with allure.step("Проверить, что  почта пользователя ="+email):
        info = main_page.get_account_info()
        assert info == email
