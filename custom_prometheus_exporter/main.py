import requests
from prometheus_client import start_http_server, Summary

# Создаем метрику, которую будем собирать
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Функция для отправки запроса
@REQUEST_TIME.time()
def make_request():
    url = "https://api.example.com/my_endpoint"
    payload = {"param1": "value1", "param2": "value2"}
    headers = {"Authorization": "Bearer MY_TOKEN"}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Запустим HTTP-сервер на 8000 порту
start_http_server(8000)

# Основной цикл программы
if __name__ == '__main__':
    while True:
        # Получим ответ от сервера
        response = make_request()

        # Добавим данные в метрику
        REQUEST_TIME.observe(response['processing_time'])

        # Выведем ответ на страницу
        print(f"Received response: {response}")