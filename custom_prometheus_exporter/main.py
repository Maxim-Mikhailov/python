from prometheus_client import Gauge, Info, Summary, Histogram, Counter, start_http_server
from http.server import HTTPServer, CGIHTTPRequestHandler
import requests
import time

#server_address = ("", 8000)
#httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
#httpd.serve_forever()

response = requests.get('http://localhost:8001/mock/free_ip.txt')

ip = Info('free_ip:', 'use_ip:')
ip.info({response.text: 'use_ip'})

# Create a metric to track time spent and requests made.
#REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.

def ip(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        print(response.text)


