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

## 2. Project Structure

```
project_root/
│── manage.py
│── requirements.txt
│── .env
│── docker-compose.yml          #Include PostgreSQL
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── blog/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
└── templates/
```

---

## 3. Installation

### 3.1 Clone the project
```bash
git clone https://github.com/username/project-name.git
cd project-name
```

### 3.2 Create a virtual environment
```bash
python -m venv venv
```

### 3.3 Activate the virtual environment
Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3.4 Install dependencies
```bash
pip install -r requirements.txt
```

---

## 4. Environment Variables

Create a `.env` file in the project root.

Example:

```env
POSTGRES_DB=django_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

---

## 5. Database Setup

### Run Postgres with Docker
```bash
docker compose up -d
```

### Apply migrations
```bash
python manage.py migrate
```

### Create superuser
```bash
python manage.py createsuperuser
```

---

## 6. Run the Development Server

```bash
python manage.py runserver
```

Server will be available at:

```
http://127.0.0.1:8000/
```

---

## 7. Example URL Structure

```
/blog/                   - List all posts
/blog/<id>/              - post detail
/users/login/            - Login page
/users/register/         - Registration
/admin/                  - Django admin
```

---

## 8. Technologies Used

- Python 3.11+
- Django 5.x
- PostgreSQL
- HTML/CSS Templates
- pip + virtualenv

---

## 9. License

This project is licensed under the MIT License.

---

