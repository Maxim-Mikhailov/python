import requests
import time
from prometheus_client import start_http_server, Gauge

# Создаем гистограмму (Gauge) метрик
request_metric = Gauge('requests_total', 'Total HTTP requests', ['method', 'endpoint'])

def collect_metrics():
    # Отправляем GET-запрос к API и получаем данные
    response = requests.get('http://yourapi.com/metrics')
    data = response.json()

    # Обновляем гистограмму
    for metric in data['metrics']:
        method = metric['method']
        endpoint = metric['endpoint']
        count = metric['count']

        request_metric.labels(method=method, endpoint=endpoint).set(count)

if __name__ == '__main__':
    # Запускаем HTTP сервер Prometheus
    start_http_server(8000)

    # Бесконечный цикл, где каждую секунду получаем метрики из API и обновляем гистограммы
    while True:
        collect_metrics()
        time.sleep(1)