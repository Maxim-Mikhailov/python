import requests
from prometheus_client import start_http_server, Gauge
import time
API_URL = 'https://example.com/api'

# Создаем метрику типа gauge и регистрируем ее
requests_metric = Gauge('requests_responses_total', 'Number of responses from an external API', ['status'])


def get_data():
    # Отправляем запрос к API
    response = requests.get(API_URL)

    # Получаем данные из ответа
    data = response.json()

    return data


def update_metrics():
    # Получаем данные из API
    data = get_data()

    # Обновляем значения метрик на основе полученных данных
    requests_metric.labels(status='success').set(data.get('success_count', 0))
    requests_metric.labels(status='failure').set(data.get('failure_count', 0))


if __name__ == '__main__':
    # Запускаем HTTP-сервер для экспонирования метрик
    start_http_server(8000)

    while True:
        # Обновляем метрики каждые 30 секунд
        update_metrics()
        time.sleep(30)