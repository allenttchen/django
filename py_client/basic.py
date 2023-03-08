import requests

#endpoint = "http://httpbin.org/status/200/"
#endpoint = "http://httpbin.org/anything"
#endpoint = "http://127.0.0.1:8000/api"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(
    endpoint,
    #params={"abc": 123},
    json={"title": "Hello world"},
) # HTTP request
print(get_response.text) # http raw text

# HTTP request returns HTML
# REST API HTTP Request -> JSON

#print(get_response.json())
#print(get_response.status_code)