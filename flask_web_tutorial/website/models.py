from . import db  # from curentt package import the db object . current package anything in int.poy file

from flask_login import UserMixin # custom class for flask login
from sqlalchemy.sql import func


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)  #db software will autoincrement to make sure alaways unique
	data = db.Column(db.String(10000))
	timestamp = db.Column(db.DateTime(), default=func.now())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(150), unique=True)   # no user can have something thats not unique
	password = db.Column(db.String(100))
	first_name =db.Column(db.String(150))
	messages = db.relationship('Message')
	


