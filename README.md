 Student Information System REST API

 Project Description

The Student Information System REST API is a secure web service developed using Django REST Framework (DRF). It provides a RESTful interface for managing student records while implementing secure authentication using JSON Web Tokens (JWT). The project also includes interactive API documentation using Swagger UI and ReDoc through drf-spectacular.

This project demonstrates how to secure REST APIs, protect endpoints, and document APIs according to the OpenAPI Specification.

 Features
 User Registration
 JWT Authentication (Login)
 Access Token Generation
 Refresh Token Generation
 Protected API Endpoints
 Student CRUD Operations
 Interactive Swagger UI Documentation
 ReDoc Documentation
 OpenAPI Schema Generation
 Django Admin Panel


 Technologies Used

 Python 3.x
 Django
 Django REST Framework (DRF)
 Simple JWT
 drf-spectacular
 SQLite (Default Database)


 Project Structure

text
studentAPI/
│
├── student_api/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md


 Installation and Setup

 Step 1: Clone the Repository

bash
git clone <repository_url>
cd studentAPI

If you are using a local project, simply navigate to the project directory.


 Step 2: Create a Virtual Environment

Windows

bash
python -m venv venv


Activate the environment:

Command Prompt

bash
venv\Scripts\activate


PowerShell

powershell
venv\Scripts\Activate.ps1



Step 3: Install Dependencies

bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install drf-spectacular


Or install from a requirements file:

bash
pip install -r requirements.txt




Step 4: Apply Database Migrations
bash
python manage.py makemigrations
python manage.py migrate




Step 5: Create a Superuser

bash
python manage.py createsuperuser


Provide:

 Username
 Email
 Password

 Step 6: Run the Development Server

bash
python manage.py runserver


Open your browser:


http://127.0.0.1:8000/



API Endpoints
 User Registration


POST /api/register/


Creates a new user account.

Example Request

json
{
    "username": "vicent",
    "email": "vicent@example.com",
    "password": "Password123!"
}




Login


POST /api/token/


Returns an Access Token and Refresh Token.

Example Request

json
{
    "username": "vicent",
    "password": "Password123!"
}




 Refresh Token


POST /api/token/refresh/


Example Request

json
{
    "refresh": "<refresh_token>"
}



 Student Endpoints

| Method | Endpoint            | Description                          |
| ------ | ------------------- | ------------------------------------ |
| GET    | /api/students/      | Retrieve all students                |
| POST   | /api/students/      | Create a student                     |
| GET    | /api/students/{id}/ | Retrieve a specific student          |
| PUT    | /api/students/{id}/ | Update all student information       |
| PATCH  | /api/students/{id}/ | Partially update student information |
| DELETE | /api/students/{id}/ | Delete a student                     |

> Note: Student endpoints require JWT authentication.



Authentication

This project uses JSON Web Token (JWT) authentication.

After logging in, include the access token in the request header:

text
Authorization: Bearer <access_token>




 API Documentation
Swagger UI


http://127.0.0.1:8000/api/swagger/


Swagger UI provides an interactive interface for exploring and testing API endpoints.


ReDoc

http://127.0.0.1:8000/api/redoc/

ReDoc presents the API documentation in a clean, readable format.


OpenAPI Schema


http://127.0.0.1:8000/api/schema/




Testing the API

Recommended tools:

 Swagger UI
 Postman
 Insomnia
*cURL



 Security Features

 JWT Authentication
 Protected API Endpoints
 Password Hashing
 Django Authentication System
 Permission-Based Access Control
 OpenAPI Documentation


 Future Improvements

 Role-Based Access Control (Admin, Lecturer, Student)
 Search and Filtering
 Pagination
 Email Verification
 Password Reset
 Profile Pictures
 PostgreSQL Support
 Deployment to a Production Server


Project: Student Information System REST API

Developed as a practical implementation of Securing and Documenting RESTful APIs Using Django REST Framework.
GROUP NO 04: MEMBERS
S/N  	FULL NAME          	    REGISTRATION NUMBER
1    	VICENT DAUDI CHACHA	        34216/T.2024
2    	ELIAS PASCHAL LUKINDO	      32705/T.2024
3    	URSULA ARTHUR MALLEY	       32458/T.2024
4    	ENOCK DOTTO MASHAURI 	      33256/T.2024
5    	ANNO ELIKIUS SWAI    	      33708/T.2024
6	    ABEID LIGWA JOHN           	33999/T.2024
7	    CECILIA STEPHEN LYELA	      33327/T.2024
8    	AHMAD YUSUPH JUMA 	         34730/T.2024
9    	SOLOMON FRANK MWANGA       	32633/T.2024
10   	PASCHAL PHAUSTINE KAPTENI  	34296/T.2024

