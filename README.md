# CRM

This repository is a simple CRM RESTful API implementation using Django Rest Framework.

## Installation

Clone this repository

    git clone https://github.com/2Fac3R/crm.git

Create and start your virtual environment [venv](https://docs.python.org/3/library/venv.html)

    python3 -m venv .env
    source .env/bin/activate

Install requirements. Use the package manager [pip](https://pip.pypa.io/en/stable/)

    pip install -r requirements.txt

Configure database in .env file (rename .env.example to .env)

    DATABASE_URL=psql://user:password@host:5432/database

Make migrations and migrate

    python3 manage.py makemigrations
    python3 manage.py migrate

Create a superuser

    python3 manage.py createsuperuser

Run the server

    python3 manage.py runserver

You can now access the API at http://127.0.0.1:8000/api/v1/

If you want to have fake data to work with, seed the database using fixtures:

    python3 manage.py loaddata [].json

I provided some fixtures with fake data, so you can do this:

    python3 manage.py loaddata organizations.json
    python3 manage.py loaddata projects.json
    python3 manage.py loaddata contacts.json
    python3 manage.py loaddata meetings.json

## Usage

Log In.

    http://127.0.0.1:8000/admin

Now you have access to the web administration site, here you can manage all the system (CRUD).

Manage models:

    http://127.0.0.1:8000/admin/crm/organization/
    http://127.0.0.1:8000/admin/crm/project/
    ...

Create a new resource:

    http://127.0.0.1:8000/admin/crm/<model>/add/

Edit a resource:

    http://127.0.0.1:8000/admin/crm/<model>/<id>/change/

Delete a resource:

    http://127.0.0.1:8000/admin/crm/<model>/<id>/delete/

Search:

    http://127.0.0.1:8000/admin/crm/<model>/?q=<search_value>

Filter:

    http://127.0.0.1:8000/admin/crm/<model>/?<field>=<value>
    http://127.0.0.1:8000/admin/crm/organization/?country=AD
                                                /?city=Walshborough
    ...
    http://127.0.0.1:8000/admin/crm/project/?<model>__id__exact=<id>
    http://127.0.0.1:8000/admin/crm/project/?organization__id__exact=1
    ...

Pagination:

    http://127.0.0.1:8000/admin/crm/<model>/?p=<page_number>
    http://127.0.0.1:8000/admin/crm/project/?p=2

## API

In order to use the API, you need to have a token session. Get one at the following endpoint:

    http://127.0.0.1:8000/api/v1/token/

Body (json):

    {
        "username": "yourusername", 
        "password": "yourpassword"
    }

This way you get 2 tokens, "refresh" and "access" tokens. 

Use access token on your API requests, and refresh token to get a new one if your access token is expired.    

    http://127.0.0.1:8000/api/v1/token/refresh/

Body (json):

    {
        "refresh": "<access_token_expired>"
    }


## Using the API
You can test the API using the http client of your preference, like curl, Postman or Insomnia.

Remember to **send the token session on each request**.

API Documentation:

    http://127.0.0.1:8000/api/v1/swagger
    http://127.0.0.1:8000/api/v1/redoc

I recommend to test the API using swagger documentation web app.

You have access to the following API routes:

    http://127.0.0.1:8000/api/v1/users/
    http://127.0.0.1:8000/api/v1/groups/
    http://127.0.0.1:8000/api/v1/organizations/
    http://127.0.0.1:8000/api/v1/projects/
    http://127.0.0.1:8000/api/v1/contacts/
    http://127.0.0.1:8000/api/v1/meetings/

## Tests

You can run all tests

    python3 manage.py test

Or individually

    python3 manage.py test crm.tests.test_<model_in_plural>
    python3 manage.py test crm.tests.test_organizations
    ...

## Description

I decided to use the following packages:

* [djangorestframework](https://www.django-rest-framework.org/) It's a powerful and flexible toolkit for building Web APIs.
* [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) Automated generation of real Swagger/OpenAPI 2.0 schemas from Django REST Framework code.
* [django-filter](https://django-filter.readthedocs.io/en/stable/) Reusable Django app allowing users to add dynamic QuerySet filtering from URL parameters.
* [django-cors-headers](https://pypi.org/project/django-cors-headers/) A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.
* [rest_framework_simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) Simple JWT is a JSON Web Token authentication plugin for the Django REST Framework.

You can find more details about others in *requirements.txt* file.

## TODO:
* Extra Web/React (in progress) or Mobile/React Native app.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Any feedback is appreciated.