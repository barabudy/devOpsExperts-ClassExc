import requests

# myDeleteResponse = requests.delete("http://localhost:8080/items/1")
response = requests.get("http://localhost:8080/items")
print(response.text)

actual = len(response.json())
expected = 2
assert expected == actual
