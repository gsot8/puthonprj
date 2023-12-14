import requests

r = requests.post("http://127.0.0.1:5000/users/create", json={"login": "surname-1", "surname": "asasasa"})
print(r.text)