import ast
import json

import requests


class ClientOilCase:

    def __init__(self, base_url: str, username: str, password: str):
        self.Base_url = base_url
        self.api_url = 'api/v1'
        self.__result = []
        self.Token = ""
        self.Token = self.login(username, password)[1:-1]

    def login(self, username: str, password: str) -> str:
        user_data = {
            'Username': username,
            'Password': password
        }
        return self.post('api/v1/Login', user_data)

    def post(self, path: str, data: dict = None, content_type='application/json;charset=utf-8') -> str:
        url = f"{self.Base_url}/{path}"
        headers = {'Authorization': f'Bearer {self.Token}',
                   'Content-type': content_type}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.content.decode("utf-8")

    def get(self, path: str) -> str:
        url = f"{self.Base_url}/{path}"
        headers = {'Authorization': f'Bearer {self.Token}'}
        response = requests.get(url, headers=headers)
        return response.content.decode("utf-8")

    def get_available_resource(self) -> any:
        url = f'{self.api_url}/CompleteMove'
        return self.get(url)

    def complete_move(self, step_count=1) -> any:
        url = f'{self.api_url}/CompleteMove?nStepsToSkip={step_count}'
        return self.post(url)

    def purchased_objects(self) -> any:
        url = f'{self.api_url}/Purchased/ObjectOfArrangement'
        return self.get(url)

    def purchased_boreholes(self) -> any:
        url = f'{self.api_url}/Purchased/Borehole'
        return self.get(url)

    def purchased_seismic(self) -> any:
        url = f'{self.api_url}/Purchased/seismic'
        return self.get(url)

    def add_result(self, data: any, name: str = None):
        name = name if name is not None else str(len(self.__result))
        try:
            self.__result.append((name, ast.literal_eval(data)))
        except:
            self.__result.append((name, data))

    def out_result(self, path):
        text = ''
        with open(path, 'w+') as file:
            text = {str(row[0]): row[1] for row in self.__result}
            json.dump(text, file)
        return text
