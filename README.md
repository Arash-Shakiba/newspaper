# 📰 Newspaper App

A newspaper web application built with Python and Django.
The project includes user authentication, custom user profiles, articles, comments, Bootstrap styling, and PostgreSQL deployment.

## ✨ Features

* 🔐 User registration, login, logout, and password management
* 👤 Custom user model with additional profile information
* 📰 Create, view, update, and delete articles
* 💬 Comment system for articles
* 🎨 Bootstrap 5 styling
* 🗄️ PostgreSQL database for production
* 🚀 Production deployment with Gunicorn and Render
* 📦 Static file handling with WhiteNoise
* 🌱 Environment variables with `environs`

## 🛠️ Tech Stack

* 🐍 Python
* 🌐 Django
* 🐘 PostgreSQL
* 🎨 Bootstrap 5
* 🔐 Django Authentication
* 🚀 Gunicorn
* 📁 WhiteNoise
* ☁️ Render

## ⚙️ Setup

Clone the repository:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add the required environment variables.

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```
## 🌐 Live Demo

The project is currently deployed on Render:

🔗 **[Live Demo](https://newspaper-gn06.onrender.com)**

> ⚠️ **Note:** This project is hosted using Render's free services. The web service may go to sleep after a period of inactivity, so the first request can take around a minute while the server starts again.

> 🗄️ **Database:** The PostgreSQL database is running on Render's free tier, which is available for **30 days**. After that, the live demo may no longer be available unless the database is upgraded or renewed.

> 🚀 **For the best experience:** If the website does not load immediately, please wait about a minute and refresh the page.
