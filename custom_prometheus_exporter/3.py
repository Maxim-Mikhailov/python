import requests

data = {"key": "value"}  # данные для отправки в формате JSON
response = requests.post(url, json=data)  # отправка запроса и получение ответа

if response.status_code == 200:  # если запрос выполнен успешно
    response_data = response.json()  # получение данных из ответа в формате JSON
    metric1 = response_data["metric1"]  # получение первой метрики из ответа
    metric2 = response_data["metric2"]  # получение второй метрики из ответа

    # вывод метрик в формате Prometheus
    print('metric1 {}\nmetric2 {}'.format(metric1, metric2))