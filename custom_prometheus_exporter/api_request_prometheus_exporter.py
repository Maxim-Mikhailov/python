import requests, json
from prometheus_client import Counter, Gauge, start_http_server

# стартуем сервер Prometheus
start_http_server(8000)

# создаем метрики для сбора статистки
c = Counter('api_request_total', 'Total number of requests to API server')
g = Gauge('api_free_ips', 'Number of free IPs returned from API server')
g2 = Gauge('api_total_ips', "Total number IPs returned from API server")

# URL API сервера
url = 'https://example/microservice/api/v1/cluster_stats/'
# запрос к api
data = {
  "msg_id": "7772fc59-453f-****-****-************",
  "correlation_id": "7772fc59-453f-****-****-************",
  "customer": "mon_di",
  "serial_number": "REGION-**********01"
}

# отправляем POST-запрос с параметром "data"
response = requests.post(url, data=json.dumps(data), verify=False, timeout=(120, 120))

# проверяем код ответа
if response.status_code == 200:
    # если запрос прошел успешно, парсим ответ и собираем значение
    result = response.json()
    free_ips = result['data']['edz']['data_free_ips']
    total_ips = result['data']['edz']['data_total_ips']
    if free_ips is not None:
        c.inc()
        g.set(free_ips)
        g2.set(total_ips)

# выводим метрики в формате Prometheus на страницу http.server
while True:
    print("api_request_total: ", c._value.get())
    print("api_free_ips: ", g._value.get())
    print("api_total_ips", g2._value.get())
