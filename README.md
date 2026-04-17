# ReST API Demo

This project includes a REST API backend, a Python Flask web app for pharmacy inventory, an HTML page for that pharmacy web app, and an HTML client for patient registration.

## HTML Client

Open the patient registration page in your browser after starting the Laravel server:

- `src/client/patient_registration.html`

The HTML client sends requests to:

- `http://127.0.0.1:8000/api/patients`

## Python Client

The Python pharmacy web client is located at:

- `src/client/pharmacy_web.py`

From the `src/client/` directory, run:

```powershell
python pharmacy_web.py
```

Then open:

- `http://127.0.0.1:5000`

The Python web client sends requests to:

- `http://127.0.0.1:5000/api/medicines`

It proxies those requests to the Laravel API at:

- `http://127.0.0.1:8000/api/medicines`

The pharmacy HTML page used by the Python web client is located at:

- `src/client/pharmacy_inventory.html`

## Setting up the database

Edit the `src/server/.env` file with the appropriate details:

```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=hospitaldb
DB_USERNAME=root
DB_PASSWORD=
```

Create the database in MySQL if it does not already exist:

```sql
CREATE DATABASE hospitaldb;
```

From the `src/server/` directory, run the database migrations:

```powershell
php artisan migrate
```

Use `migrate:fresh` to start from scratch.

## Running Locally

From the `src/server/` directory, start the Laravel development server:

```powershell
php artisan serve
```

Then:

- open `src/client/patient_registration.html` in your browser
- run `python pharmacy_web.py` from `src/client/`
- open `http://127.0.0.1:5000` for the pharmacy web app

The Laravel API runs by default at:

- `http://127.0.0.1:8000`
