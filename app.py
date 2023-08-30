from flask import Flask


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@127.0.0.1:3306/School"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True 


from controllers import *
from extensions import *
from models import *


if __name__== "__main__":
    app.run(port=5000, debug=True)
