import requests

data = {data}
url = "http://206.189.232.135:4000/api/v1/products"

response = requests.post(url, data)
print(response)

