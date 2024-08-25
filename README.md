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
     
4. **Install dependencies:**

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

**Auth**
Base URL: `http://127.0.0.1:8000/api/user/`

- **Register User:** `POST register/`
- **Login User:** `POST login/`
- **Refresh Token:** `POST token/refresh/`
- **User Profile:** `GET profile/`
- **Update User:** `PATCH update/`


**Farms**
Base URL: `http://127.0.0.1:8000/api/farm/`


- **List all farms:** `GET /farms/`
- **Create a new farm:** `POST /farms/`
- **Retrieve a specific farm:** `GET /farms/{id}/`
- **Update a specific farm:** `PUT /farms/{id}/`
- **Partially update a specific farm:** `PATCH /farms/{id}/`
- **Delete a specific farm:** `DELETE /farms/{id}/`

**Crops**

- **List all crops for farms owned by the authenticated user:** `GET /crops/`
- **Create a new crop:** `POST /crops/`
- **Retrieve a specific crop:** `GET /crops/{id}/`
- **Update a specific crop:** `PUT /crops/{id}/`
- **Partially update a specific crop:** `PATCH /crops/{id}/`
- **Delete a specific crop:** `DELETE /crops/{id}/`

**Animals**

- **List all animals for farms owned by the authenticated user:** `GET /animals/`
- **Create a new animal:** `POST /animals/`
- **Retrieve a specific animal:** `GET /animals/{id}/`
- **Update a specific animal:** `PUT /animals/{id}/`
- **Partially update a specific animal:** `PATCH /animals/{id}/`
- **Delete a specific animal:** `DELETE /animals/{id}/`
