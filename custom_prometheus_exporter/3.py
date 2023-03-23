import requests

data = {"key": "value"}  # данные для отправки в формате JSON
response = requests.post(url, json=data)  # отправка запроса и получение ответа

if response.status_code == 200:  # если запрос выполнен успешно
    response_data = response.json()  # получение данных из ответа в формате JSON
    metric1 = response_data["metric1"]  # получение первой метрики из ответа
    metric2 = response_data["metric2"]  # получение второй метрики из ответа

    # вывод метрик в формате Prometheus
    print('metric1 {}\nmetric2 {}'.format(metric1, metric2))

    import http.server
    import urllib.parse
    import urllib.request

    PORT = 8000


    class MyHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'<html><body><h1>GET Request Received!</h1></body></html>')

        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            data = urllib.parse.urlencode({'key': 'value'}).encode('ascii')
            response = urllib.request.urlopen(url="your_api_url", data=data).read()
            response_data = response.decode('ascii')

            self.wfile.write(bytes(response_data, "utf-8"))


    httpd = http.server.HTTPServer(('localhost', PORT), MyHandler)

    print("serving at port", PORT)
    httpd.serve_forever()