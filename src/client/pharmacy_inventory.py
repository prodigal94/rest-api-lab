import requests

BASE_URL = "http://127.0.0.1:8000/api/medicines"

def create_medicine(name, stock_quantity, unit_price):
    response = requests.post(BASE_URL, json={
        "name": name,
        "stock_quantity": stock_quantity,
        "unit_price": unit_price
    }, headers={"Accept": "application/json"})
    return response

def get_all_medicines():
    response = requests.get(BASE_URL)
    return response

def get_medicine(medicine_id):
    response = requests.get(f"{BASE_URL}/{medicine_id}")
    return response

def update_medicine(medicine_id, name=None, stock_quantity=None, unit_price=None):
    data = {}
    if name: data["name"] = name
    if stock_quantity: data["stock_quantity"] = stock_quantity
    if unit_price: data["unit_price"] = unit_price
    response = requests.post(f"{BASE_URL}/{medicine_id}", json=data, headers={
        "Accept": "application/json",
        "Content-Type": "application/json"
    }, params={"_method": "PUT"})
    return response

def delete_medicine(medicine_id):
    response = requests.delete(f"{BASE_URL}/{medicine_id}")
    return response

if __name__ == "__main__":
    print("Pharmacy Inventory System")
    while True:
        print("\n1. Add Medicine")
        print("2. View All Medicines")
        print("3. View Medicine by ID")
        print("4. Update Medicine")
        print("5. Delete Medicine")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            stock = int(input("Stock Quantity: "))
            price = float(input("Unit Price: "))
            resp = create_medicine(name, stock, price)
            print(f"Status: {resp.status_code}")
            if resp.status_code == 201:
                print("Medicine added successfully!")
            else:
                print(resp.json())

        elif choice == "2":
            resp = get_all_medicines()
            print(f"Status: {resp.status_code}")
            medicines = resp.json()
            for med in medicines:
                print(f"ID: {med['id']}, Name: {med['name']}, Stock: {med['stock_quantity']}, Price: {med['unit_price']}")

        elif choice == "3":
            med_id = int(input("Medicine ID: "))
            resp = get_medicine(med_id)
            print(f"Status: {resp.status_code}")
            if resp.status_code == 200:
                med = resp.json()['data']
                print(f"ID: {med['id']}, Name: {med['name']}, Stock: {med['stock_quantity']}, Price: {med['unit_price']}")
            else:
                print(resp.json())

        elif choice == "4":
            med_id = int(input("Medicine ID: "))
            name = input("New Name (leave blank to skip): ") or None
            stock = input("New Stock Quantity (leave blank to skip): ")
            stock = int(stock) if stock else None
            price = input("New Unit Price (leave blank to skip): ")
            price = float(price) if price else None
            resp = update_medicine(med_id, name, stock, price)
            print(f"Status: {resp.status_code}")
            if resp.status_code == 200:
                print("Medicine updated successfully!")
            else:
                print(resp.json())

        elif choice == "5":
            med_id = int(input("Medicine ID: "))
            resp = delete_medicine(med_id)
            print(f"Status: {resp.status_code}")
            if resp.status_code == 200:
                print("Medicine deleted successfully!")
            else:
                print(resp.json())

        elif choice == "6":
            break

        else:
            print("Invalid choice!")