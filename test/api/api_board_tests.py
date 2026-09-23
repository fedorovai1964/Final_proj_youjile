import allure
from api.BoardApi import BoardApi

api = BoardApi()
@allure.severity(allure.severity_level.CRITICAL)

def test_get_boards():
    board_list = api.get_all_boards()

    assert len(board_list['content']) == board_list['paging']['count']


def test_get_board_by_id(board):
    id_board, name = board
    data_board = api.find_board(id_board)
    with allure.step("Проверить, что заголовок"
                     " созданной доски совпадает с заданным"):
        assert data_board['title'] == name


def test_create_board(board):
    id_board, name = board
    data_board = api.find_board(id_board)
    with allure.step("Проверить, что заголовок"
                     " созданной доски совпадает с заданным"):
        assert data_board['title'] == name


def test_update_board(board):
    id_board, name = board

    new_name = f"{name} измененная"
    api.update_board(id_board, new_name)

    data_board = api.find_board(id_board)
    with allure.step("Проверить, что заголовок изменился"):
        assert data_board['title'] == new_name


def test_delete_board(board):
    id_board, name = board
    board_list_before = api.get_all_boards()

    api.delete_board(id_board)
    board_list_after = api.get_all_boards()

    id_after = [b['id'] for b in board_list_after['content']]
    with allure.step("Проверить, что удаленной доски нет в списке"):
        assert id_board not in id_after

    with (allure.step("Проверить, количество досок уменьшилось на единицу")):
        assert len(board_list_before['content']
                   ) - len(board_list_after['content']) == 1
