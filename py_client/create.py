import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    "title": "This field is nice",
    'price': 32.99,
}
get_response = requests.post(
    endpoint,
    #params={"abc": 123},
    json=data,
)
print(get_response.json())
