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
2. Ensure you have pip installed (it should comes with python packages)
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
1. GET (/)
2. GET (/swagger)
3. POST (/register)
4. POST (/login)
5. *Protected-Bearer GET (/protected)
6. *Protected-Bearer GET (/users)


# Design Summary

## Reason for the design

## Libraries Used

1. Flask - Framework (Python)
2. Sqlite3 - Database (flask default)
3. 

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
Here you should say what actually happens when you execute the code above.
