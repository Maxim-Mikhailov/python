import requests
from prometheus_client import Counter, Gauge, start_http_server

# стартуем сервер Prometheus
start_http_server(8000)

# создаем метрики для сбора статистки
c = Counter('api_request_total', 'Total number of requests to API server')
g = Gauge('api_free_ips', 'Number of free IPs returned from API server')

# URL API сервера
url = 'https://api.example.com'

# отправляем POST-запрос с параметром "data"
response = requests.post(url, data={'some_data': 123})

# проверяем код ответа
if response.status_code == 200:
    # если запрос прошел успешно, парсим ответ и собираем статистику
    result = response.json()
    free_ips = result.get('free_ips')
    if free_ips is not None:
        c.inc()
        g.set(free_ips)

# выводим метрики в формате Prometheus на страницу http.server
while True:
    print("api_request_total: ", c._value.get())
    print("api_free_ips: ", g._value.get())