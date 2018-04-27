from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    public_uid = db.Column(db.String(255),unique=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    api_key = db.relationship('API_Key', backref='user', lazy="dynamic")  # ,uselist=False)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.name}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class API_Key(db.Model):
    __tablename__ = 'apikeys'
    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(255), unique=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
