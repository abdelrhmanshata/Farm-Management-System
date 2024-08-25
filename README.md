# Farm Management System

## Overview
The Farm Management System is a Django-based application that provides secure access to farm data management using JWT authentication.

## Setup and Installation
### Prerequisites

- Python 3.x
- Django 3.x or higher
- Dependencies listed in `requirements.txt`

### Installation
1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    
2. **Create and activate a virtual environment:**
    On Linux,
    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```
    On Windows
    ```bash
    virtualenv venv
    venv\Scripts\activate
    ```
     
3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Apply database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. **Create a superuser (for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

### Running the Project

1. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

2. **Access the API endpoints and admin interface:**

    - **API Endpoints:** Customize based on your API.
    - **Admin Interface:** Accessible at `http://localhost:8000/admin/`

### Example API Endpoints

- **Register User:** `POST api/user/register/`
- **Obtain Token:** `POST api/user/login/`
- **Refresh Token:** `POST api/user/token/refresh/`
- **User Profile:** `GET api/user/profile/`
- **Update User:** `PATCH api/user/update/`

