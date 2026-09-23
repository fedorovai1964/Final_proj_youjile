import allure
from pages.MainPage import MainPage


def test_pages_available_tasks(browser, auth):

    main_page = MainPage(browser)

    with allure.step("Открыть страницу my tasks"):
        main_page.get_tasks()

    current_url = main_page.get_current_url()
    with allure.step(
            "Проверить, что URL=" + current_url + "оканчивается на /my-tasks"):
        assert current_url.endswith("my-tasks")


def test_pages_available_projects(browser, auth):
    main_page = MainPage(browser)

    with allure.step("Открыть страницу my company"):
        main_page.get_company()

    current_url = main_page.get_current_url()
    with allure.step(
            "Проверить, что URL=" + current_url + "оканчивается на /projects"):
        assert main_page.get_current_url().endswith("projects")
