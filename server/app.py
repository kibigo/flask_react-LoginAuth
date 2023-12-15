from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from models import db, User
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)


@app.route('/@me')
def get_current_user():
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({
            "error":"Unauthorized"
        }),401
    
    user = User.query.filter_by(id = user_id).first()
    return jsonify({
        "id": user.id,
        "email":user.email
    })


@app.route('/register', methods = ['POST'])

def register_user():

    email = request.json['email']
    password = request.json['password']

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



@app.route('/login', methods = ['POST'])

def login_user():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email = email).first()

    if user is None:
        
        return jsonify({
            "error" : "Unauthorized"
        }),401
    
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "unauthorized"}),401
    
    session["user_id"] = user.id
    
    return jsonify({
        "id": user.id,
        "email":user.email
    })


if __name__ == "__main__":
    app.run(debug=True)
    