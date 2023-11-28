from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from models import db, User


app = Flask(__name__)

bcrypt = Bcrypt(app)

migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hehegrgrooqur'



@app.route('/register', method = ['POST'])

def register_user():

    email = request.json('email')
    password = request.json('password')

    user_exists = User.query.filter_by(email = email).first() is not None

    if user_exists:
        return jsonify({
            "error": "User already exist"
        })

    hashed_password = bcrypt.generate_password_hash(password)

    new_user = User(email = email, password = hashed_password)

    db.session.add(new_user)
    db.session.commit()


    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })