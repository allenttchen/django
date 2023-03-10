import requests

endpoint = "http://localhost:8000/api/product/"

get_response = requests.get(
    endpoint,
    #params={"abc": 123},
    #json=data,
)
print(get_response.json())
