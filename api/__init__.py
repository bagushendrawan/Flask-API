from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, getenv
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

SWAGGER_URL="/swagger"
API_URL="/static/swagger.yaml"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)

db = SQLAlchemy()
DB_NAME = 'project.db'

def create_app():
    app = Flask(__name__)
    CORS(app)
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECRET_KEY'] = getenv('SECRET_KEY', 'default_secret_key')
    app.config['WTF_CSRF_CHECK_DEFAULT'] = False

    db.init_app(app)
    create_database(app)
    

    return app

def create_database(app):
    if not path.exists('instance/'+DB_NAME):
        print("Path not exist")
        with app.app_context():
            db.create_all()
        print('Database Created!')
    else:
        print("Db already exist")

    