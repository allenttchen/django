import requests

endpoint = "http://localhost:8000/api/product/1/"

get_response = requests.get(
    endpoint,
    #params={"abc": 123},
    #json={"title": "Hello world"},
)
print(get_response.json())
