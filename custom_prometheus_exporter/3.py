import requests
from prometheus_client import start_http_server, Gauge

# Создаем Gauge метрики Prometheus
metric1 = Gauge('metric1', 'Описание метрики 1')
metric2 = Gauge('metric2', 'Описание метрики 2')

# Отправляем GET-запрос к REST API и получаем данные
response = requests.get('https://example.com/api')
data = response.json()

# Обрабатываем данные и передаем их в формате Prometheus
metric1.set(data['value1'])
metric2.set(data['value2'])

# Запускаем Prometheus HTTP-сервер на порту 8000
start_http_server(8000)







import requests
from prometheus_client import start_http_server, Gauge

# создаём объект Gauge (метрика)
response_time_metric = Gauge('api_response_time_seconds', 'Response time of API in seconds')

# направляем GET-запрос к REST API и измеряем время ответа
def get_api_data():
    try:
        response = requests.get(url='https://example.com/api', timeout=10)
        response_time = response.elapsed.total_seconds()
        if response.status_code == 200:
            json_data = response.json()
            return json_data, response_time
        else:
            return None, response_time
    except requests.exceptions.RequestException as e:
        print(e)
        return None, 0

# обрабатываем данные и передаём их в Prometheus метрику
def process_data():
    data, response_time = get_api_data()
    if data is not None:
        # производим дальнейшую обработку данных в формате JSON
        pass
    response_time_metric.set(response_time)

# запускаем HTTP-сервер Prometheus на порту 8000 и производим обработку данных
if __name__ == '__main__':
    start_http_server(8000)
    while True:
        process_data()


import requests
from prometheus_client import start_http_server, Gauge

# Создаем метрику для хранения ответа REST API
response_metric = Gauge('response_metric', 'Response metric description')

# Функция для выполнения GET-запроса к REST API и получения ответа в JSON-формате
def get_api_response():
    response = requests.get('https://api.example.com/')
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Функция для обновления метрики с новыми значениями из REST API
def update_metrics():
    api_response = get_api_response()
    if api_response:
        response_metric.set(api_response['metric_value'])

# Запускаем HTTP-сервер Prometheus экспортера
start_http_server(8000)

# Бесконечный цикл для обновления метрик каждую минуту
while True:
    update_metrics()
    time.sleep(60)


import requests
from prometheus_client import Gauge, start_http_server

# Создаем метрику
REQUESTS_POST_METRIC = Gauge('requests_post_metric', 'Запрос на API POST', ['status_code'])

# Отправляем POST-запрос и выводим ответ в виде метрики
def request_post(url, data):
    resp = requests.post(url, data=data)
    REQUESTS_POST_METRIC.labels(status_code=resp.status_code).inc()
    return resp.text

# Запускаем сервер для метрик Prometheus
if __name__ == '__main__':
    start_http_server(8000)

    # Выполняем POST-запросы и выводим ответы в виде метрик
    url = 'http://example.com/api'
    data = {'key': 'value'}
    response = request_post(url, data)

