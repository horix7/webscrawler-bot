import requests
import json

products = json.load(open("/home/paul/Documents/projects/PythonBoto/scrape/allProducts.json"))

validProducts = [ int(i.price) for i in products]

print(validProducts[0])
# for product in products:
#     headers = {
#     'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoxLCJmaXJzdE5hbWUiOiJKb2huIiwicGhvbmUiOiIxMzEzMjQyMyIsImxvY2F0aW9uIjoicndhbmRhICIsImxhc3ROYW1lIjoiRG9lIiwiZW1haWwiOiJwYXVsQGVtYWlsLmNvbSIsImlzQWRtaW4iOnRydWUsImNyZWF0ZWRBdCI6IjIwMjEtMDQtMDlUMTE6MTI6MjYuMjczWiIsInVwZGF0ZWRBdCI6IjIwMjEtMDQtMDlUMTE6MTI6MjYuMjczWiJ9LCJpYXQiOjE2MTc5NjY4ODUsImV4cCI6MTYxOTc2Njg4NSwiYXVkIjoiIiwiaXNzIjoiUmVzdGZ1bCBFY29tbWVyY2UifQ.WkX42tdfM2DwwUaUaZQryVBPqrdCe-osp75pmCgk8ao",
#     'cache-control': "no-cache",
#     'postman-token': "b5f2957a-178c-512c-3843-a6825685e0e2",
#     'content-type': "application/x-www-form-urlencoded"
#     }
#     url = "http://206.189.232.135:4000/api/v1/products"

#     response = requests.request("POST", url, data=product, headers=headers)
    
#     print(response.text)

print(len(products))