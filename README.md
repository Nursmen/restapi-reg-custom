# Django REST API Registration Custom

This repository contains a custom implementation of a Django-based REST API for user registration and authentication. It uses **Django Rest Framework (DRF)** and includes features such as user registration, login, and token-based authentication.

## Features

- User registration with validation
- Token-based authentication (JWT)
- User login functionality
- Django Rest Framework (DRF) powered API
- Customizable registration logic

## Requirements

To run this project, ensure you have the following installed:

- Python 3.7+
- Django
- Django Rest Framework (DRF)
- Simple JWT for JWT token management

You can install the dependencies by running:

```bash
pip install -r requirements.txt
```

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/Nursmen/restapi-reg-custom.git
   ```

2. Navigate to the project directory:

   ```bash
   cd restapi-reg-custom
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database by running migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

| Endpoint           | Method | Description                     |
|--------------------|--------|---------------------------------|
| `/api/register/`   | POST   | Register a new user             |
| `/api/login/`      | POST   | Login and receive a JWT token   |
| `/api/users/me/`   | GET    | Retrieve the logged-in user's info |

## Example Requests

### Register a new user

```http
POST /api/register/
Content-Type: application/json
{
  "username": "newuser",
  "password": "password123",
  "email": "newuser@example.com"
}
```

### Login

```http
POST /api/login/
Content-Type: application/json
{
  "username": "newuser",
  "password": "password123"
}
```

Response:

```json
{
  "access_token": "eyJhbGciOiJI...",
  "token_type": "bearer"
}
```

### Get User Info

```http
GET /api/users/me/
Authorization: Bearer <access_token>
```

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to this project.

## License

This project is licensed under the NO License
