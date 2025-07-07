# DjangoBlog App

A clean and simple blog platform built using Django and MySQL.

This project is designed to help developers understand Django fundamentals like views, templates, URL routing, models, admin customization, and database integration with MySQL.

## 🔧 Features

- 📝 Create, read, update, delete (CRUD) blog posts
- 🔒 Admin panel to manage posts
- 🌐 Dynamic routing with slugs
- 🎨 HTML templating with Bootstrap (optional)
- 🗃️ MySQL integration with Django ORM

## 🚀 Tech Stack

- Python 3
- Django 4.x
- MySQL 8
- HTML/CSS (for templating)
- Git/GitHub

## 📦 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/djangoblog-app.git
cd djangoblog-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up database (using MySQL)
# Configure settings.py → DATABASES with your MySQL user/password

# Apply migrations
python manage.py migrate

# Start the development server
python manage.py runserver
