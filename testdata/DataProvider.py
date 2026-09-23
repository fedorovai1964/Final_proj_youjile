import json
my_file = open('testdata/test_data.json')

global_data = json.load(my_file)


class DataProvider:
    def __init__(self) -> None:
        self.data = global_data

    def get(self, prop: str):
        return self.data.get(prop)

    def get_email(self) -> str:
        return self.data.get("email")

    def get_password(self) -> str:
        return self.data.get("password")
