import requests
from prometheus_client import Gauge, start_http_server
import time

API_URL = 'https://example.com/api/metrics'

# Создаем метрики типа Gauge и регистрируем их
request_duration = Gauge('request_duration_seconds', 'API request duration in seconds')
response_size = Gauge('response_size_bytes', 'API response size in bytes')


def get_metrics():
    # Отправляем запрос к API и получаем ответ
    response = requests.get(API_URL)
    data = response.json()

    # Получаем данные из ответа и обновляем значения метрик
    request_duration.set(data['request_duration'])
    response_size.set(data['response_size'])


if __name__ == '__main__':
    # Запускаем HTTP-сервер для экспонирования метрик
    start_http_server(8000)

    while True:
        # Обновляем метрики каждые 30 секунд
        get_metrics()
        time.sleep(30)