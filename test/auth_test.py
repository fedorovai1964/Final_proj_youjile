from config import email
from config import password
import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from time import sleep

def test_auth(browser, auth):
    auth_page = AuthPage(browser)

    with allure.step("Проверить, что в верхней строке загруженной страницы есть надпись 'My company'"):
        assert auth_page.сompany_search() == "My company"

    main_page = MainPage(browser)
    main_page.open_menu()

    current_url = main_page.get_current_url()
    with allure.step("Проверить, что  URL=" + current_url+ "заканчивается на ..../..account"):
        assert current_url.endswith("account")

    with allure.step("Проверить, что  почта пользователя на вкладке учетных данных ="+email):
        info = main_page.get_account_info()
        assert  info == email


