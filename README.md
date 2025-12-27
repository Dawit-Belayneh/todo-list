# 📝 Todo App Backend (Django REST API)

A powerful **Todo Application Backend** built with **Django REST Framework**, featuring **authentication**, **categories**, **repeating tasks**, and **background reminders using Celery & Redis**.

---

## 🚀 Features

### ✅ Core Features
- User authentication (Token-based)
- Create, read, update, delete todos
- Each user sees **only their own todos**
- Categories (One category → many todos)
- Search, filter, and ordering
- Due date & due time (AM / PM supported)

### 🔁 Repeating Tasks
- No repeat
- Daily
- Weekly
- Monthly
- Automatically creates the next task when completed

### 🔔 Notifications & Reminders
- Reminder before due time
- Background processing using **Celery**
- Redis as message broker
- Periodic task checking (Celery Beat)

---

## 🛠 Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **Celery**
- **Redis**
- **SQLite** (can be switched to PostgreSQL)
- **Token Authentication**

---

## 🔐 Authentication

- Token-based authentication
- Login returns a token
- Use token in requests:


---

## 📌 API Endpoints (Example)

### Auth
- `POST /api/signup/`
- `POST /api/login/`

### Todos
- `GET /api/todos/`
- `POST /api/todos/`
- `GET /api/todos/{id}/`
- `PUT /api/todos/{id}/`
- `DELETE /api/todos/{id}/`

### Categories
- `GET /api/categories/`
- `POST /api/categories/`

---

## 🔍 Filtering, Searching & Ordering

### Filter by category

### Search (title, description, category name)

### Order by date

---

## ⏰ Repeating Tasks Logic

- Each todo has a `repeat` field:
  - `none`, `daily`, `weekly`, `monthly`
- When a repeating task is marked **completed**, a new task is auto-created using Django signals.

---

## 🔔 Celery & Redis Setup

### Install dependencies
```bash
pip install celery redis django-celery-beat
run
redis-server
python manage.py migrate
celery -A todo_app worker -l info
Future Improvements

Email / push notifications

Task priority levels

Calendar view integration

Shared tasks between users

Production deployment (Docker, PostgreSQL)
Integrate with frontend soon

