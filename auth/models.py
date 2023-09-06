from flask_login import UserMixin
from flask_security import RoleMixin
from werkzeug.security import generate_password_hash

from extensions import db, login_manager

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)  
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255), nullable = True)

roles_users = db.Table("roles_users",
                       db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
                       db.Column("role_id", db.Integer(), db.ForeignKey("role.id")))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(200))
    name =  db.Column(db.String(30))
    surname =  db.Column(db.String(50))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


    def __init__(self, email, password, name, surname) -> None:
        self.email = email
        self.password = generate_password_hash(password, method="sha256")
        self.name = name
        self.surname = surname


    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    @property
    def full_name(self) -> str:
        return f"{self.name} {self.surname}"
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)