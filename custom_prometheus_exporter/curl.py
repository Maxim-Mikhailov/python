import requests
#зависимость которая забирает значение курлом и отображает его в нужном виде

response = requests.get('http://localhost:8001/mock/free_ip.txt')
print(response.text)
