import requests
from prometheus_client import Metric, REGISTRY, CollectorRegistry, push_to_gateway
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily

class MyExporter(object):
    def collect(self):
        response = requests.get('https://api.example.com')
        json_data = response.json()

        metric = GaugeMetricFamily('example_metric', 'Example metric description', labels=['label1'])
        metric.add_metric(['value1'], json_data['value'])

        yield metric

if __name__ == '__main__':
    registry = CollectorRegistry()
    registry.register(MyExporter())
    push_to_gateway('localhost:9091', job='my_job', registry=registry)





