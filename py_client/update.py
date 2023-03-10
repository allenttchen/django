import requests

endpoint = "http://localhost:8000/api/product/1/update/"

data = {
    "title": "Hello world",
    "price": 129.99
}

get_response = requests.put(
    endpoint,
    #params={"abc": 123},
    json=data,
)
print(get_response.json())
