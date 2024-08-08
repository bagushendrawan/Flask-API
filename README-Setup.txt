# Flask - Rest API

- Github Repository Link :
https://github.com/bagushendrawan/Flask-API

- Railway deployment Link :
https://flask-api-production-6584.up.railway.app/

- Swagger API Documentation :
https://flask-api-production-6584.up.railway.app/swagger

## Installing / Getting started

A quick introduction of the minimal setup you need to get a hello world up &
running.

1. Install Python : https://www.python.org/downloads/
2. Ensure you have pip installed (it should have comes with python packages)
3. Create python virtual environment

  Command :
  pip install virtualenv
  python<version> -m venv <virtual-environment-name>

4. Run virtual environment (ensure the virtual environment is running)
   
  For Mac :
  source <your_venv_name>/bin/activate
  
  For Windows :
  <your_venv_name>/Scripts/activate


5. Install required dependencies
   
  Command :
  pip install -r requirements.txt

6. Run flask app
   
  Command :
  flask --app main run

## API Routes
1. GET (/) - Hello World Pages
2. GET (/swagger) - API Documentation

3. POST (/register) - Register User

  (x-www-form-urlencoded)
  - username : Unique, Min=2, Max=20
  - email : Unique, Valid Email, Max=150
  - password : Min=8, Max=64
  
4. POST (/login) - Login User & Get JWT

  (x-www-form-urlencoded)
  - username
  - password

(Bearer Auth)
5. *Protected-Bearer GET (/protected) - Protected Endpoint Check
6. *Protected-Bearer GET (/users) - Get All User Registered

