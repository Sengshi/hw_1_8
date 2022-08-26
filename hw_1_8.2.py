from os import path
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        response = requests.get(f'{url}/upload?path={path.basename(file_path)}&overwrite=True', headers=headers).json()
        with open(file_path, 'r') as f:
            try:
                requests.put(response['href'], files={'file': f})
                print(f'Файл {path.basename(file_path)} успешно загружен!')
            except KeyError:
                print(response)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '/Users/aloster/PycharmProjects/hw_1_8/test.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)