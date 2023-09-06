from flask import Flask

from datetime import timedelta

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@127.0.0.1:3306/School"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True 
app.config["SECRET_KEY"] = "bf9a4a8a8dad8bc035e0aec46ab4bbff" 
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=300)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

from extensions import *


if __name__== "__main__":
    from student.models import *
    from blog.models import *
    from auth.models import *

    from student.controllers import student as student_bp
    from auth.controllers import auth as auth_bp

    from admin import *

    app.register_blueprint(student_bp, url_prefix="/students")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.run(host="localhost", port=5000, debug=True)

