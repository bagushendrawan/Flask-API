from sqlalchemy.exc import IntegrityError
from flask import Blueprint, request, jsonify, make_response,current_app
from wtforms import StringField, PasswordField, Form
from wtforms.validators import DataRequired, Email, Length
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask_swagger import swagger
from . import db
from .models import User

views = Blueprint('views', __name__)

class RegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])


def require_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        bearer = request.headers.get('Authorization')

        if bearer and bearer.startswith('Bearer '):
            token = bearer.split()[1]
        else:
            token = None

        if not token:
            return jsonify({'message' : 'Token is missing, please add to bearer authorization'}), 401
  
        try:
            print('secret', current_app.config['SECRET_KEY'])
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(username = data['username']).first()
        except:
            return jsonify({
                'message' : 'Token is invalid, please try again'
            }), 401

        return  f(*args, **kwargs)
  
    return decorated

@views.route("/spec")
def spec():
    """
        Create a new user
        ---
        tags:
          - users
        definitions:
          - schema:
              id: User
              properties:
                name:
                 type: string
                 description: the user's name
        parameters:
          - in: body
            name: body
            schema:
              id: User
              required:
                - email
                - username
              properties:
                email:
                  type: string
                  description: email for user
                username:
                  type: string
                  description: name for user
        responses:
          201:
            description: User created
        """
    return jsonify(swagger(current_app))

@views.route("/")
def index():
    return "<p>Hello, World!</p>"

@views.route("/login", methods=['POST'])
def login_post():
    form = request.form
    if not form or not form.get('username') or not form.get('password'):
        return make_response(
            'Could not login, please check all the fields',
            400,
        )

    user = User.query.filter_by(username = form.get('username')).first()

    if not user:
        return make_response(
            'User not found!',
            400
        )

    if check_password_hash(user.password, form.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'username': user.username,
            'exp' : datetime.now() + timedelta(minutes = 60)
        }, current_app.config['SECRET_KEY'], algorithm="HS256")

        return make_response(jsonify({'token' : token, 'decode' : jwt.decode(token,current_app.config['SECRET_KEY'],algorithms=["HS256"])}), 201)
    
    return make_response(
            'Password or username may be incorrect',
            400
        )


@views.route("/register", methods=['POST'])
def register_post():
    form = RegistrationForm(request.form)
    if form.validate():
        try:
            user = User(username=form.username.data, email=form.email.data, password=generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
        except IntegrityError as e:
            print("ERRORRS")
            db.session.rollback()  # Rollback the session to avoid further issues
            if 'UNIQUE constraint' in str(e.orig):  # Check if the error is related to unique constraint
                # This message can be customized based on your needs
                return jsonify({"error": "Username or email already exists."}), 400
            else:
                # For other database errors
                return jsonify({"error": "An error occurred while registering the user."}), 500
        return f"<p>{user.username} is registered successfully!</p>"
    else:
        return {"errors": form.errors}, 400

@views.route("/protected")
@require_token
def protected():
    return "<p>Hello Verified Users!</p>"

@views.route("/users")
@require_token
def get_all_users():
    users = User.query.all()  # Get all users
    return {
        "users": [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email
            } for user in users
        ]
    }