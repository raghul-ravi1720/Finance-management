# 💰 Finance Management Application

A full-stack **Finance Management Web Application** built using **Django** and **PostgreSQL**. This app helps users efficiently track, manage, and analyze their income and expenses through an intuitive dashboard and detailed reports.

---

## 🚀 Features

- 🔐 User authentication (sign up, login, logout)
- 💵 Add, edit, and delete income and expense transactions
- 📊 Category-wise financial breakdown
- 📈 Monthly and yearly expense reports
- 📅 Calendar view for transaction tracking
- 🔍 Search and filter transactions
- 📁 Export data as CSV
- Responsive UI using Bootstrap

---

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: PostgreSQL
- **Other Tools**: Django Admin, Django ORM, Chart.js

---

## 📸 Screenshots

(Add screenshots of your dashboard, forms, charts, etc. here.)

---

## 📂 Project Structure
finance_app/ ├── manage.py ├── finance_app/ │ ├── settings.py │ ├── urls.py │ └── wsgi.py ├── tracker/ │ ├── models.py │ ├── views.py │ ├── urls.py │ └── templates/ └── static/




---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```
   git clone https://github.com/your-username/finance-management-app.git
   cd finance-management-app
   ```

2. **Create Virtual Environment**
   ```
   python -m venv venv

   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

5. **Configure PostgreSQL Database**

- Create a PostgreSQL database and user.
- Update your settings.py with DB credentials:

    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'your_db_name',
          'USER': 'your_db_user',
          'PASSWORD': 'your_password',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }


6. **Run Migrations**
```
python manage.py makemigrations
python manage.py migrate
```

7. **Start the Server**
```
python manage.py runserver
```
