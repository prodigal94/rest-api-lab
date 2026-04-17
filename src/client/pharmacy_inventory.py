import os

import requests


BASE_URL = os.getenv("PHARMACY_API_URL", "http://127.0.0.1:8000/api/medicines")


def parse_response(response):
    try:
        return response.json()
    except ValueError:
        return {"message": response.text or "No response body returned."}


def format_api_error(payload):
    if isinstance(payload, dict):
        message = payload.get("message")
        errors = payload.get("errors")
        if isinstance(errors, dict) and errors:
            details = []
            for field, field_errors in errors.items():
                details.append(f"{field}: {', '.join(str(error) for error in field_errors)}")
            return f"{message} | {'; '.join(details)}" if message else "; ".join(details)
        if message:
            return str(message)
    return str(payload)


def collect_medicine_fields(require_all_fields):
    name_input = input("Name: " if require_all_fields else "New Name (leave blank to skip): ").strip()
    stock_input = input(
        "Stock Quantity: " if require_all_fields else "New Stock Quantity (leave blank to skip): "
    ).strip()
    price_input = input(
        "Unit Price: " if require_all_fields else "New Unit Price (leave blank to skip): "
    ).strip()

    data = {}

    if require_all_fields or name_input:
        if not name_input:
            raise ValueError("Name is required.")
        data["name"] = name_input

    if require_all_fields or stock_input:
        if not stock_input:
            raise ValueError("Stock quantity is required.")
        stock_quantity = int(stock_input)
        if stock_quantity < 0:
            raise ValueError("Stock quantity must be 0 or greater.")
        data["stock_quantity"] = stock_quantity

    if require_all_fields or price_input:
        if not price_input:
            raise ValueError("Unit price is required.")
        unit_price = round(float(price_input), 2)
        if unit_price < 0:
            raise ValueError("Unit price must be 0 or greater.")
        data["unit_price"] = unit_price

    return data


def create_medicine(name, stock_quantity, unit_price):
    return requests.post(
        BASE_URL,
        json={
            "name": name,
            "stock_quantity": stock_quantity,
            "unit_price": unit_price,
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )


def get_all_medicines():
    return requests.get(BASE_URL, headers={"Accept": "application/json"})


def get_medicine(medicine_id):
    return requests.get(f"{BASE_URL}/{medicine_id}", headers={"Accept": "application/json"})


def update_medicine(medicine_id, name=None, stock_quantity=None, unit_price=None):
    data = {}
    if name is not None:
        data["name"] = name
    if stock_quantity is not None:
        data["stock_quantity"] = stock_quantity
    if unit_price is not None:
        data["unit_price"] = unit_price

    return requests.put(
        f"{BASE_URL}/{medicine_id}",
        json=data,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )


def delete_medicine(medicine_id):
    return requests.delete(f"{BASE_URL}/{medicine_id}", headers={"Accept": "application/json"})


if __name__ == "__main__":
    print("Pharmacy Inventory System")
    print(f"Using API: {BASE_URL}")
    print("This Python client specifically manages medicines.")

    while True:
        print("\n1. Add Medicine")
        print("2. View All Medicines")
        print("3. View Medicine by ID")
        print("4. Update Medicine")
        print("5. Delete Medicine")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                data = collect_medicine_fields(require_all_fields=True)
            except ValueError as error:
                print(f"Input error: {error}")
                continue

            resp = create_medicine(data["name"], data["stock_quantity"], data["unit_price"])
            print(f"Status: {resp.status_code}")
            if resp.status_code == 201:
                medicine = parse_response(resp)
                print(
                    f"Medicine added successfully: "
                    f"ID {medicine['id']} | {medicine['name']} | "
                    f"Stock {medicine['stock_quantity']} | Price {medicine['unit_price']}"
                )
            else:
                print(format_api_error(parse_response(resp)))

        elif choice == "2":
            resp = get_all_medicines()
            print(f"Status: {resp.status_code}")
            medicines = parse_response(resp)
            if resp.status_code != 200:
                print(format_api_error(medicines))
                continue

            for med in medicines:
                print(
                    f"ID: {med['id']}, Name: {med['name']}, "
                    f"Stock: {med['stock_quantity']}, Price: {med['unit_price']}, "
                    f"Created: {med.get('created_at', 'N/A')}"
                )

        elif choice == "3":
            med_id = int(input("Medicine ID: "))
            resp = get_medicine(med_id)
            print(f"Status: {resp.status_code}")
            payload = parse_response(resp)
            if resp.status_code == 200:
                med = payload.get("data", {})
                print(
                    f"ID: {med['id']}, Name: {med['name']}, "
                    f"Stock: {med['stock_quantity']}, Price: {med['unit_price']}, "
                    f"Created: {med.get('created_at', 'N/A')}"
                )
            else:
                print(format_api_error(payload))

        elif choice == "4":
            med_id = int(input("Medicine ID: "))
            try:
                data = collect_medicine_fields(require_all_fields=False)
            except ValueError as error:
                print(f"Input error: {error}")
                continue

            if not data:
                print("Nothing to update. Provide at least one field.")
                continue

            resp = update_medicine(
                med_id,
                data.get("name"),
                data.get("stock_quantity"),
                data.get("unit_price"),
            )
            print(f"Status: {resp.status_code}")
            if resp.status_code == 200:
                medicine = parse_response(resp).get("data", {})
                print(
                    f"Medicine updated successfully: "
                    f"ID {medicine['id']} | {medicine['name']} | "
                    f"Stock {medicine['stock_quantity']} | Price {medicine['unit_price']}"
                )
            else:
                print(format_api_error(parse_response(resp)))

        elif choice == "5":
            med_id = int(input("Medicine ID: "))
            resp = delete_medicine(med_id)
            print(f"Status: {resp.status_code}")
            if resp.status_code == 200:
                print(parse_response(resp).get("message", "Medicine deleted successfully!"))
            else:
                print(format_api_error(parse_response(resp)))

        elif choice == "6":
            break

        else:
            print("Invalid choice!")
