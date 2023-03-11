
# File Upload REST API using Django and DRF

    This project implements a REST API for uploading a CSV 
    file containing data for billions of records. 
    The project uses Django and Django Rest Framework (DRF) 
    to handle the API requests and PostgreSQL as the database.

## Requirements
    Python 3.6 or higher
    Django 3 or higher
    Django Rest Framework (DRF) 3 or higher
    PostgreSQL 10.0 or higher

## Getting Started
Clone the repository to your local machine.  
Install the required Python packages by running pip install -r requirements.txt in your terminal.  
Create a PostgreSQL database for the project.  
Set the database connection details in settings.py.  
Run the database migrations by running python manage.py migrate in your terminal.  
Start the Django development server by running python manage.py runserver in your terminal.  
Open your web browser and navigate to http://localhost:8000 to access the API documentation.  
Uploading a File.  
To upload a file, send a POST request to the /files/ endpoint with the file field set to the CSV file you want to upload.   
The API will process the file and insert the records into the database.

## Example Request:

#### makefile
POST /files/

Headers:
Content-Type: multipart/form-data

Body:
file: <CSV File>
Example Response:

###  HTTP/1.1 201 CREATED
Content-Type: application/json

    {
        "id": 1,
        "file": "example.csv",
        "status": "processed",
        "created_at": "2023-03-11T14:30:00Z"
    }   
Searching and Sorting Records.  

    To search for records, send a GET request to the /users/ endpoint with the search parameters in the query string.
    You can search by first_name, last_name, phone_number, email, and birth_date. 
    You can also sort the results by any of these fields.


Example Request:

GET /users/?search=john&sort_by=birth_date

Headers:
Content-Type: application/json
Example Response:

json
    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "first_name": "norbert",
                "last_name": "lupamo",
                "national_id": "29690069",
                "birth_date": "1990-01-01",
                "address": "Nairobi",
                "country": "Kenya",
                "phone_number": "714-123567",
                "email": "norbert@norbert.com",
                "finger_print_signature": "a1b2c3d4e5"
            },
            {
                "first_name": "faith",
                "last_name": "faith",
                "national_id": "29123456",
                "birth_date": "1995-01-01",
                "address": "Ongata rongai",
                "country": "Kenya",
                "phone_number": "715-123456",
                "email": "faith@faith.com",
                "finger_print_signature": "f6g7h8i9j0"
            }
        ]
    }
## Unit Tests
The project includes unit tests to ensure the API functions as expected.                
You can run the tests by running python manage.py test in your terminal.

## Pre-Commit Hook
The project includes a pre-commit hook that runs black and flake8
