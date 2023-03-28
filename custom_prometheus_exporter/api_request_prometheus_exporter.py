import requests
import json
from time import sleep
from prometheus_client import Counter, Gauge, start_http_server

# Стартуем сервер Prometheus
start_http_server(8000)

# Создаем метрики для сбора статистики
c = Counter('api_request_total', 'Total number of requests to API server')
g_free_ips = Gauge('api_free_ips', 'Number of free IPs returned from API server')
g_total_ips = Gauge('api_total_ips', "Total number IPs returned from API server")
c_req_failed = Counter('api_request_failed_total', 'Total number of failed requests to API server')

# URL API сервера
url = 'https://example/microservice/api/v1/cluster_stats/'

while True:
    # Запрос к API
    data = {
      "msg_id": "7772fc59-453f-****-****-************",
      "correlation_id": "7772fc59-453f-****-****-************",
      "customer": "mon_di",
      "serial_number": "REGION-**********01"
    }
    response = requests.post(url, data=json.dumps(data), verify=False, timeout=(120, 120))
    # Проверяем код ответа
    if response.status_code == 200:
        # Если запрос прошел успешно, парсим ответ и собираем значение
        result = response.json()
        free_ips = result['data']['edz']['data_free_ips']
        total_ips = result['data']['edz']['data_total_ips']
        if free_ips is not None:
            c.inc()
            g_free_ips.set(free_ips)
            g_total_ips.set(total_ips)
    else:
        # Если запрос не прошел успешно, увеличиваем счетчик неудачных запросов
        c_req_failed.inc()

    # Выводим метрики в формате Prometheus на страницу http.server
    print("api_request_total: ", c._value.get())
    print("api_request_failed_total: ", c_req_failed._value.get())
    print("api_free_ips: ", g_free_ips._value.get())
    print("api_total_ips", g_total_ips._value.get())
    sleep(30)