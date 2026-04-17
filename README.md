# ReST API Demo

This project includes a REST API backend and a simple HTML client for patient registration.

## HTML Client

Open the patient registration page in your browser after starting the Laravel server:

- `http://127.0.0.1:8000/patient_registration.html`

The HTML client is located at `src/server/public/patient_registration.html`.

## Setting up the database

Edit the `src/server/.env` file with the appropriate details:

From the `src/server/` directory, run the database migrations:

```bash
php artisan migrate
```

Use `migrate:fresh` to start from scratch. 

## Running Locally

From the `src/server/` directory, start the Laravel development server:

```bash
php artisan serve
```

Then visit the patient registration page at the URL above.

