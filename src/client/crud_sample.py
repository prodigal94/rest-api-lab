import requests

# CREATE
response = requests.post(
	"http://localhost:8000/api/medicines/",
	json = {
		"name": "Paracetamol",
		"stock_quantity": 100,
		"unit_price": 10
	},
    headers = {
        "Accept": "application/json"
    }
)
print(response.status_code)
print(response.json())

# READ (all)
response = requests.get("http://localhost:8000/api/medicines")
print(response.status_code)
print(response.json())

latest_addition = response.json()[-1]

# READ (1)
response = requests.get(f"http://localhost:8000/api/medicines/{latest_addition['id']}")
print(response.status_code)
print(response.json())

# UPDATE
response = requests.post(
    f"http://127.0.0.1:8000/api/medicines/{latest_addition['id']}",
    json = {
		"stock_quantity": 50,
        "_method": "PUT"
	}, 
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    },
    allow_redirects = False
)
print(response.status_code)
print(response.json())

# DELETE
response = requests.delete(f"http://localhost:8000/api/medicines/{latest_addition['id']}")
print(response.status_code)
print(response.json())