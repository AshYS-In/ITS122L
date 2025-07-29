# ITS122L Project - Information Hub

A Django-based web application for managing announcements, events, and user profiles.

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** installed on your system
- **Git** (for cloning the repository)
- **PostgreSQL** (optional - the project uses a remote database)

### Installation & Setup

1. **Clone or Download the Project**
   ```bash
   # If you have the project files, navigate to the project directory
   cd "C:\Users\User\Downloads\ITS122L_Project-main\ITS122L_Project-main"
   ```

2. **Activate the Virtual Environment**
   
   **On Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   **On Windows (Command Prompt):**
   ```cmd
   venv\Scripts\activate.bat
   ```
   
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django psycopg
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - **Main Application**: http://127.0.0.1:8000/
   - **Admin Interface**: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
ITS122L_Project-main/
├── manage.py              # Django management script
├── project/               # Main Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # WSGI configuration
├── info_hub/             # Main application
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── urls.py           # App URL routing
│   ├── templates/        # HTML templates
│   └── static/           # CSS, JS, images
├── venv/                 # Virtual environment
└── db.sqlite3           # Local database (if using SQLite)
```

## 🔧 Configuration

### Database
The project is configured to use PostgreSQL with a remote database. The connection settings are in `project/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "verceldb",
        "USER": "default",
        "PASSWORD": "bjQ0m4taruIS",
        "HOST": "ep-lucky-bonus-a11h7iyc-pooler.ap-southeast-1.aws.neon.tech",
        "PORT": "5432"
    }
}
```

### Environment Variables
For production, consider moving sensitive information to environment variables.

## 🛠️ Development Commands

### Useful Django Commands

```bash
# Run the development server
python manage.py runserver

# Run on a specific port
python manage.py runserver 8080

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Open Django shell
python manage.py shell
```

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Use a different port
   python manage.py runserver 8080
   ```

2. **Database Connection Issues**
   - Check your internet connection
   - Verify the database credentials in `settings.py`
   - Consider using SQLite for local development

3. **Virtual Environment Issues**
   ```bash
   # Recreate virtual environment
   python -m venv venv
   # Then activate and install dependencies
   ```

4. **Static Files Not Loading**
   ```bash
   python manage.py collectstatic
   ```

5. **Migration Issues**
   ```bash
   # Reset migrations (WARNING: This will delete data)
   python manage.py migrate --fake-initial
   ```

### Switching to SQLite (Local Development)

If you want to use SQLite instead of PostgreSQL for local development:

1. **Update settings.py**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

2. **Run migrations**
   ```bash
   python manage.py migrate
   ```

## 📱 Features

- **User Authentication**: Login, registration, and profile management
- **Announcements**: Create and manage announcements
- **Events**: Event management system
- **Admin Interface**: Django admin for content management
- **Responsive Design**: Mobile-friendly interface

## 🔒 Security Notes

- The project is configured for development (`DEBUG = True`)
- For production deployment, set `DEBUG = False`
- Move sensitive information to environment variables
- Use HTTPS in production

## 📞 Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Verify all prerequisites are installed
3. Ensure the virtual environment is activated
4. Check the Django documentation: https://docs.djangoproject.com/

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure a production database
3. Set up static file serving
4. Use a production WSGI server (Gunicorn, uWSGI)
5. Configure your web server (Nginx, Apache)

---

**Happy Coding! 🎉** 