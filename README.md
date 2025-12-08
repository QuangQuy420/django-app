# Django Project

A basic Django project with a clean structure, PostgreSQL database, and modular apps.  
This project is suitable for learning, practicing, or building production-ready backend services.

---

## 1. Features

- Django 5.x
- PostgreSQL database integration
- Modular app structure (users, blog)
- Django Admin customization
- Authentication and Authorization
- CRUD operations with Django ORM
- Environment variables via `.env`
- Templates and static file configuration

---

## 2. How to Start the Application with Docker (Recommended for WSL or Linux environments)

### 2.1. Clone the project
```bash
git clone git@github.com:QuangQuy420/django-app.git
cd django-app.git
```

### 2.2. Configure .env (Edit if any)
```bash
cp .env.example .env
```

### 2.3. Build and Start
```bash
docker compose up --build
```

### 2.4. Apply Migrations
```bash
docker compose exec web python manage.py migrate
```

### 2.5. Create Superuser (Optional)
```bash
docker compose exec web python manage.py createsuperuser
```

### You can now access your API at http://localhost:8000/blog

---

## 3. How to start application with Windows

### 3.1. Clone the project
```bash
git clone git@github.com:QuangQuy420/django-app.git
cd django-app.git
```

### 3.2. Create a virtual environment
```bash
python -m venv venv
```

### 3.3. Activate the virtual environment
Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3.4. Install dependencies
```bash
pip install -r requirements.txt
```

### 3.5. Configure .env (Edit if any)
```bash
cp .env.example .env
```

### 3.6. Database Setup
#### Download the PostgreSQL Installer for Windows.
- During installation, set the password to 123456 (to match your .env) or update your .env later.
- Open pgAdmin (installed with Postgres) or a terminal and create a database named django_db.


### 3.7. Apply migrations
```bash
python manage.py migrate
```

### 3.8. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 3.9. Run the Development Server

```bash
python manage.py runserver
```

### You can now access your API at http://localhost:8000/blog

---

## 4. Example URL Structure

```
/blog/                   - List all posts
/blog/<id>/              - post detail
/users/login/            - Login page
/users/register/         - Registration
/admin/                  - Django admin
```

---

## 5. Technologies Used

- Python 3.11+
- Django 5.x
- PostgreSQL
- HTML/CSS Templates
- pip + virtualenv

---

## 6. License

This project is licensed under the MIT License.

---

