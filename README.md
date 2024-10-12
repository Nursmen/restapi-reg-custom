# REST API Registration Custom

This repository provides a custom implementation of a REST API for user registration and management. It is built using **FastAPI** and includes features such as user registration, login, and token-based authentication.

## Features

- User registration with validation
- Token-based authentication (JWT)
- User login functionality
- Customizable registration logic
- Lightweight and fast API with FastAPI

## Requirements

To run this project, ensure you have the following installed:

- Python 3.7+
- FastAPI
- Uvicorn
- SQLAlchemy (for database management)
- JWT (for token management)

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

5. Run the application using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

| Endpoint           | Method | Description                     |
|--------------------|--------|---------------------------------|
| `/register`        | POST   | Register a new user             |
| `/login`           | POST   | Login and receive a JWT token   |
| `/users/me`        | GET    | Retrieve the logged-in user's info |

## Example Requests

### Register a new user

```http
POST /register
Content-Type: application/json
{
  "username": "newuser",
  "password": "password123",
  "email": "newuser@example.com"
}
```

### Login

```http
POST /login
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
GET /users/me
Authorization: Bearer <access_token>
```

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to this project.

## License

This project is licensed under the NO License.
