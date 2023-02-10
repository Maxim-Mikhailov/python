from prometheus_client import start_http_server, Summary
import random
import time

# Создание метрики для остлеживания затраченного времени и отслеживания запросов
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# декорация функции метрикой
@REQUEST_TIME.time()
def process_request(t):
    """функция обманка которая требует немного времени"""
    time.sleep(t)

if __name__ == '__main__':
    # старт сервера
    start_http_server(8000)
    # генерация запросов
    while True:
        process_request(random.random())