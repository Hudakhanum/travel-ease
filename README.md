# 🌍 TravelEase – Travel Agent Web App

TravelEase is a simple full-stack web application that allows users to explore and book travel packages, while giving admins the ability to manage packages and view bookings.

---

## ✨ Features

### 👤 For Users:
- Browse available travel packages
- View details like destination, price, and description
- Book a package by entering name and email
- Receive booking confirmation

### 👩‍💼 For Admins:
- Add new travel packages
- Edit or delete existing packages *(optional)*
- View a list of all customer bookings

---

## 💡 User Stories

### As a Visitor:
- I want to browse travel packages so I can choose my next trip.
- I want to see package details like price and destination.
- I want to book a package by filling out a form.
- I want confirmation after booking a package.

### As an Admin:
- I want to add new travel packages so I can promote new trips.
- I want to edit or delete outdated packages.
- I want to view all bookings made by users so I can manage reservations.

---

## 🛠 Tech Stack

| Layer     | Tech Used         |
|-----------|-------------------|
| Frontend  | HTML, CSS, JavaScript *(Bootstrap optional)* |
| Backend   | Python + Flask    |
| Database  | SQLite (using SQL queries) |
| API Test  | Postman or Fetch  |

---

## 🗂 Project Structure

travel-ease/
├── app.py # Flask app entry point
├── database.py # DB initialization script
├── models.py # DB helper functions
├── travel.db # SQLite database
├── templates/ # HTML files (if using Flask templating)
├── static/ # CSS/JS files
└── README.md # This file


📁 Folder & File Setup Summary
rust
Copy
Edit
travel-ease/
│
├── app/
│   ├── __init__.py      ← Setup Flask app
│   ├── routes.py        ← Define web routes
│   ├── models.py        ← Will be for database
│   ├── templates/
│   │   └── index.html   ← Home page HTML
│   └── static/          ← CSS, JS files (empty for now)
│
├── run.py               ← Entry point to run the app
├── config.py            ← (We’ll use later)
├── README.md            ← Already created
├── requirements.txt     ← Installed Python packages
├── venv/                ← Your virtual environment
