#  Nakala Api 

#### This an API endpoint Based on Django  ,  15/09/2021

#### By **Eston Kagwima**

## Description
This is an API endpoint based on Django that allows a user to 

- Signup.
- Send email upon signup.
- Validate email signup
- Login using username & password.
- Fetch data from a Postgres database.  data used https://covid.ourworldindata.org/data/owid-covid-data.csv
- Display the data by querying an API.
- Sign-out

This project was generated with [Django](https://docs.djangoproject.com/en/3.2/) version 3.2.7



## Setup/Installation Requirements
- install Python3.9
- Clone this repository `https://github.com/kagus-code/Nakala-Analyze.git`
- Change directory to the project directory using  the `cd` command
- Open project on VSCode
- If you want to use virtualenv: `virtualenv ENV && source ENV/bin/activate`
- run: `pip install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE <name>;
####  .env file
Create .env file and paste paste the following and fill  required fields:

    SECRET_KEY = '<Secret_key>'
    DBNAME = '<name>'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
    DB_HOST='127.0.0.1'
    MODE='dev'
    ALLOWED_HOSTS='*'
    DISABLE_COLLECTSTATIC=1
    EMAIL_USE_TLS=True
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_HOST_USER=''
    EMAIL_HOST_PASSWORD=''
    EMAIL_PORT=587
#### Run initial Migration
    python3.9 manage.py makemigrations <name of the app>
    python3.9 manage.py migrate
#### Run the app
    python3.9 manage.py runserver
    Open terminal on localhost:8000
    Access the different api endpoints by editing the url


## Technologies Used

- Django version 3.2.7
- Python
- PostgresSQL
- Django REST Framework

## link to live site on heroku
https://nakala-analyze.herokuapp.com/
## Support and contact details

| Eston | ekagwima745@gmail.com |
| ----- | --------------------- |

## API ENDPOINTS
 1. api/users/register/
    This endpoint allows you to sign up and recieve a confirmation email on sign up
  2. api/users/login/
    This endpoint allows you to log in and obtain an auth token only after confirming your email
 3. api/data/query/<id>/
    This endpoint allows you to query the data by id
 api/data/query/<iso_code>/
    This end point allows you to query the data by iso_code
### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Eston Kagwima