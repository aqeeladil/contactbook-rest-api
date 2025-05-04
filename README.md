# Contact Book API

This project is an API for managing a user's contact list. Users can register, log in, and manage their contacts with the ability to create, update, view, search, and delete contacts. Authentication is handled using JWT (JSON Web Token), and the API is fully documented using **DRF Spectacular** for easy access.

---

## 🔧 Features

- **JWT Authentication** – Login, register, and secure all contact data per user.
- **CRUD Contacts** – Create, read, update, and delete your personal contacts.
- **Search & Filter** – Filter contacts by `name` or `email`.
- **Pagination** – Default page size of 5 contacts.
- **Interactive Docs** – Swagger & ReDoc docs available via DRF Spectacular.
- **Admin Panel** – Manage data through Django's admin interface.
- **CORS Support** – Ready to connect with frontend frameworks like React or Vue.

---

## Technologies Used

- **Python**: The core language for the backend.
- **Django**: The web framework used for developing the API.
- **Django REST Framework (DRF)**: To build RESTful APIs.
- **Simple JWT**: For JWT authentication and token management.
- **DRF Spectacular**: To generate and serve API documentation.
- **CORS Headers**: To allow cross-origin requests from the frontend.
- **Postgresql**: Database for storing user and contact data.
- **django-environ** (for `.env` config)

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/aqeeladil/contactbook-rest-api.git
cd contactbook-rest-api

# Create a virtual environment
python -m venv venv
source venv/Scripts/activate

# Install the dependencies
pip install -r requirements.txt

# Set up the environment variables:
# Create a .env file at the root of the project and add the following content:
SECRET_KEY=your-strong-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CORS_ALLOWED_ORIGINS=http://localhost:3000
DB_NAME=your_db_name
DB_USER=your_postgres_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Run migrations to set up the database:
cd contactbook
python manage.py migrations
python manage.py migrate

# Create a superuser to access the Django admin (optional):
python manage.py createsuperuser

python manage.py runserver

# Your application should now be live at http://127.0.0.1:8000/api.
```

---

## 📘 API Endpoints

Test the endpoints using tools like Postman.

```markdown
| Endpoint                           | Description                        |
|------------------------------------|------------------------------------|
| `POST /api/token/`                | Get JWT token pair                 |
| `POST /api/token/refresh/`        | Refresh access token               |
| `GET /api/contacts/`              | List contacts                      |
| `POST /api/contacts/`             | Create a new contact               |
| `GET /api/contacts/<id>/`         | Retrieve a specific contact        |
| `PUT /api/contacts/<id>/`         | Update a specific contact          |
| `DELETE /api/contacts/<id>/`      | Delete a specific contact          |
| `GET /api/schema/`                | Get OpenAPI schema (raw)           |
| `GET /api/docs/`                  | Swagger UI                         |
| `GET /api/redoc/`                 | ReDoc UI                           |
```
