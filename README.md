<img src="./api/static/logo.png" alt="Logo of the project" align="right" width=64 height=64>

# Flask - Rest API

## Github Repository

```shell
https://github.com/bagushendrawan/Flask-API
```

## Railway deployment

```shell
https://flask-api-production-6584.up.railway.app/
```

## Swagger API Documentation

```shell
https://flask-api-production-6584.up.railway.app/swagger
```

![image](https://github.com/user-attachments/assets/a85943e3-3de6-4013-9b06-eee69d4f450d)



## Installing / Getting started

A quick introduction of the minimal setup you need to get a hello world up &
running.

1. Install Python : https://www.python.org/downloads/
2. Ensure you have pip installed (it should have comes with python packages)
3. Create python virtual environment

```shell
pip install virtualenv
python<version> -m venv <virtual-environment-name>
```

4. Run virtual environment (ensure the virtual environment is running)
   
```shell
//Mac
source env/bin/activate

//Windows
<your_venv_name>/Scripts/activate
```

5. Install required dependencies
   
```shell
pip install -r requirements.txt
```

6. Run flask app
   
```shell
flask --app main run
```

## API Routes
1. GET (/) - Hello World Pages
2. GET (/swagger) - API Documentation

4. POST (/register) - Register User

   Body : (x-www-form-urlencoded)
   - username : Unique, Min=2, Max=20
   - email : Unique, Valid Email, Max=150
   - password : Min=8, Max=64
    
6. POST (/login) - Login User & Get JWT

   Body : (x-www-form-urlencoded)
   - username
   - password

6. *Protected-Bearer GET (/protected) - Protected Endpoint Check

    Headers : (Bearer Auth)
   <br/>
   "Bearer <token_from_login>
   
8. *Protected-Bearer GET (/users) - Get All User Registered

    Headers : (Bearer Auth)
   <br/>
   "Bearer <token_from_login>


# Design Summary

## Reason for the design

- Flask
<p>The main reason i chose Flask as the framework is that they are very minimal & lightweight, much like Express JS. Additionally, it helps me to learn more about Python web development, because you would have to manually set most of the functionality.</p>

- Sqlite3
<p>It's simple built-in databases system, self-contained and require minimal setup.</p>

- Werkzeug
<p>It's simple security library used for password hashing and check, could be change to other library like bcrypt</p>

- WTForms
<p>Form & form fields library, used mainly for its validator, could be implemented to frontend if any </p>

As the reason above suggest, my approach to this API design is how it would require minimal setup for the deployment and also met all the criteria required. In addition, my decision for this approach is that would help me to learn more about python web development from the scratch before moving on to High Level Framework like Django. *As a notes i have disabled the CSRF token requirement just for this project because of some errors

## Libraries Used

1. Flask - Framework (Python)
2. Sqlite3 - Database (flask default database)
3. Sqlalchemy - Database toolkit and ORM
4. WTForms - Form & form fields (validator)
5. Watchdog - Development kit
6. Werkzeug - Hash Password
7. PyJWT - JSON Web Token
8. Swagger - API Documentation
9. Waitress - Server Railway Deployment

```shell
//requirements.txt
blinker==1.8.2
click==8.1.7
colorama==0.4.6
dnspython==2.6.1
email_validator==2.2.0
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
flask-swagger==0.2.14
flask-swagger-ui==4.11.1
Flask-WTF==1.2.1
greenlet==3.0.3
gunicorn==22.0.0
idna==3.7
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
packaging==24.1
PyJWT==2.9.0
python-dotenv==1.0.1
PyYAML==6.0.2
SQLAlchemy==2.0.32
typing_extensions==4.12.2
waitress==3.0.0
watchdog==4.0.1
Werkzeug==3.0.3
WTForms==3.1.2
```


## Challenges

- Adapt
<p>My very first challenge for this project is that i have never used python for web development before, which have quite different approach and syntax than using Javascript or Typescript. Because of it, i have to learn from scratch all the framework and library used for this project. Fortunately, it has the same core concepts than Express which helps me quite a lot.</p>

- Design
<p>I'm quite struggling to decide on how i would build this project. Before using flask, i have tried using Django to complete this test. But to my surprise, it mostly have an built-in functionality provided (which makes me feel bad) and quite lot of initial setup which you could found here.</p>

<a href="https://github.com/bagushendrawan/Django-Technical-Test">Django Prototype</a> <br/>
<p>For that reason, i'm pivotting my decision and start the project from scratch using Flask.</p>
