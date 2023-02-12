from prometheus_client import Gauge, Info, Summary, Histogram, Counter, start_http_server
import requests
import time

response = requests.get('http://localhost:8001/mock/free_ip.txt')

ip = Info('free_ip:', 'use_ip:')
ip.info({response.text: ''})

def ip(t):
#    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        print(response.text)







