# Sake Forum

A Django-based web application for sharing and reviewing Japanese sake experiences.

## Core Features

1. **Post Creation**
   - User-friendly form to create sake reviews
   - Fields include:
     - Nickname
     - Sake Name (日本酒名)
     - Rating (1-5 stars)
     - Review content (感想)
     - Purchase location (購入場所)
     - Drinking occasion (飲んだシーン)
     - Image upload support

2. **Post Display**
   - Clean card-based layout
   - Star rating visualization
   - Metadata displayed in Japanese style with gray brackets
   - Image support with responsive design

3. **Data Model**
   - Structured data storage
   - Support for optional fields
   - Automatic timestamp creation

## Technical Details

1. **Form Implementation**
   - Bootstrap-based styling
   - Custom field labels in Japanese
   - File upload handling
   - Form validation

2. **Views**
   - Class-based ListView for posts
   - Function-based view for post creation
   - Pagination support (10 posts per page)

3. **Internationalization**
   - Japanese language support
   - Tokyo timezone
   - Japanese date format

## Project Structure
- Django 3.2.25
- Bootstrap 5.3.0 for frontend
- SQLite database
- Media file handling for images


## Setup Requirements

### 1. Environment Setup

Create a virtual environment:
```bash
python3 -m venv venv
```

Activate the virtual environment:

- **On macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```
- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```

Install required packages:
```bash
pip install django==3.2.25
pip install Pillow  # for image handling
```

---

### 2. Project Configuration

1. **Clone** the repository and **navigate** to the project directory.  
2. **Create** required directories:
   ```bash
   mkdir media
   mkdir static
   ```
3. **Update `settings.py`:**
   ```python
   # Update SECRET_KEY with a secure key
   SECRET_KEY = 'your-secret-key'

   # Set DEBUG appropriately
   DEBUG = True  # For development
   DEBUG = False # For production

   # Configure ALLOWED_HOSTS if needed
   ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
   ```

*(Setup)*

---

### 3. Database Setup

Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser (optional):
```bash
python manage.py createsuperuser
```

*(Application)*

---

### 4. Running the Application

Start the development server:
```bash
python3 manage.py runserver
```

Access the application at:
```
http://127.0.0.1:8000/
```

---

### 5. Additional Configuration

- Ensure proper permissions for `media` and `static` directories.  
- Configure your web server (e.g., Nginx, Apache) for production.  
- Set up proper security measures before deployment.  
- Configure database settings in `settings.py` if using a different database.


## Future Improvements
1. User authentication
2. Search functionality
3. Sake categories
4. Comment system
5. API endpoints