from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_admin import Admin

from app import app

csrf = CSRFProtect(app)

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

admin = Admin(app, name = "Student's blogs", template_mode='bootstrap3')

db = SQLAlchemy(app)
migrate = Migrate(app, db) 
