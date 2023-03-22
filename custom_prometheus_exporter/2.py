import requests
from prometheus_client import CollectorRegistry, Gauge, pushadd_to_gateway

# Создаем гистограмму метрик
metric = Gauge('metric', 'Metric collected from API', ['label1', 'label2'])

# Создаем объект коллектора регистра, чтобы отправить данные в Prometheus
registry = CollectorRegistry()

# Отправляем GET-запрос к API и получаем данные в JSON формате
response = requests.get('https://example.com/api')
json_data = response.json()

# Обрабатываем данные и добавляем метрики в гистограмму
for data in json_data:
    label1 = data['label1']
    label2 = data['label2']
    value = data['value']

    # Устанавливаем значение метрики в гистограмме с помощью метода set()
    metric.labels(label1=label1, label2=label2).set(value)

# Отправляем метрики в Prometheus
pushadd_to_gateway('localhost:9091', job='myjob', registry=registry)