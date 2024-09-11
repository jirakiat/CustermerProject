
# Customer Management System

This is a Django-based web application for managing customer data and locations. The system includes features like adding, editing, deleting, and viewing customers with SweetAlert confirmations.

## Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **MySQL** (or other supported database)

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set Up a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

In `settings.py`, update the `DATABASES` section with your MySQL credentials.

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Key URLs

- **Add Customer**: `http://127.0.0.1:8000/customer/add_customer/`
- **Show Customers**: `http://127.0.0.1:8000/customer/customer_list/`
