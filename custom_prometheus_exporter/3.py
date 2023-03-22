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




