from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

# Адрес, на котором будет доступна веб-страница
HOST_NAME = '127.0.0.1'
PORT_NUMBER = 8000

# URL для запроса к API
API_URL = "https://example.com/api"


# Функция, которая делает POST запрос к API, получает два значения в ответе и выводит их в нужном формате для Prometheus
def collect_data():
    response = requests.post(API_URL, json={'data1': 'value1', 'data2': 'value2'})

    # Получение значений из ответа
    value1 = response.json().get('data1')
    value2 = response.json().get('data2')

    # Вывод данных в формате, который использует Prometheus для сбора метрик
    output = "# HELP custom_metric_1 Description of custom_metric_1\n# TYPE custom_metric_1 gauge\ncustom_metric_1{value=\"" + str(
        value1) + "\"} " + str(value1) + "\n"
    output += "# HELP custom_metric_2 Description of custom_metric_2\n# TYPE custom_metric_2 gauge\ncustom_metric_2{value=\"" + str(
        value2) + "\"} " + str(value2) + "\n"

    return output


# Класс запроса
class MyHandler(BaseHTTPRequestHandler):

    # Ответ на GET запрос
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Получение данных с помощью функции collect_data() и их вывод
        data = collect_data()
        self.wfile.write(data.encode())
        return


# Запуск веб-сервера
if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    print('Server started on port', PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Server stopped.')



from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/metrics':
            response = requests.post('https://example.com/api/endpoint', data={'param1': 'value1', 'param2': 'value2'})
            data = response.json()

            metrics = f'my_metric{{param1="{data["param1"]}",param2="{data["param2"]}"}} 1\n'

            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; version=0.0.4; charset=utf-8')
            self.end_headers()
            self.wfile.write(metrics.encode('utf-8'))
        else:
            self.send_response(404)


server = HTTPServer(('127.0.0.1', 8000), MyRequestHandler)
server.serve_forever()