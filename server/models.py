from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


metadata = MetaData()

db = SQLAlchemy(metadata=metadata)



class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.String(32), primary_key = True, unique = True)
    email = db.Column(db.String(345), unique = True)
    password = db.Column(db.Text, nullable=False)