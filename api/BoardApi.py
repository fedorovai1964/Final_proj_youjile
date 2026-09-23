import requests
import allure
from faker import Faker
from config import headers
from configuration.ConfigProvider import ConfigProvider
fake = Faker()


class BoardApi():

    def __init__(self) -> None:
        self.__url = ConfigProvider().get_api_url()
        self.project_id = ConfigProvider().get_project_id()

    @staticmethod
    def random_board_name() -> str:
        """Метод для создания случайного имени доски"""
        return f"Пробная доска: {fake.catch_phrase()}"

    @allure.step("Получить список всех досок")
    def get_all_boards(self) -> dict:
        """Метод GET для получения списка всех досок"""
        url = self.__url + "/boards"

        response = requests.request("GET", url, headers=headers)
        return response.json()

    @allure.step("Создать доску")
    def create_board(self, name: str) -> dict:
        """Метод POST для создания новой доски"""
        url = self.__url + "/boards"
        payload = {
            'title': name,
            'projectId': self.project_id,
            'stickers': {
                'timer': False,
                'deadline': True,
                'stopwatch': True,
                'timeTracking': True,
                'assignee': True,
                'repeat': True
                }
            }
        response = requests.request("POST", url, json=payload, headers=headers)
        return response.json()

    @allure.step("Получить доску по ID")
    def find_board(self, id_board: str) -> dict:
        """Метод GET для получения доски по ID"""
        url = self.__url + "/boards/" + id_board
        response = requests.request("GET", url, headers=headers)
        return response.json()

    @allure.step("Изменить название доски по id")
    def update_board(self, id_board: str, name: str):
        """Метод PUT для изменения доски"""
        url = self.__url + "/boards/" + id_board
        payload = {
            'title': name,
            'projectId': self.project_id,
            'stickers': {
                'deadline': True,
                'assignee': True
                }
            }
        response = requests.request("PUT", url, json=payload, headers=headers)

        return response.json()

    @allure.step("Удалить доску")
    def delete_board(self, id_board: str):
        """Метод PUT для получения удаления доски"""
        url = self.__url + "/boards/" + id_board

        payload = {
            'deleted': True,
            }
        response = requests.request("PUT", url, json=payload, headers=headers)
        return response.json()
