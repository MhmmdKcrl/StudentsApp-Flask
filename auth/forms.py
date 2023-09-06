from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError, Length, EqualTo

from auth.models import User


def custom_blacklist_checker(form, field):
    with open("utils/black_list_emails.txt") as f:
        for i in f.readlines():
            if field.data.endswith(i):
                raise ValidationError("This email is in blacklist, You can not login")

def custom_user_checker(form, field):
    user = User.query.filter_by(email = field.data).first()
    if not user:
        raise ValidationError("Account can not found!")


class LoginForm(FlaskForm):
    email = EmailField("Emailinizi daxil edin", validators = [DataRequired(),
                                                              custom_blacklist_checker,
                                                              custom_user_checker])
    password = PasswordField("Parolu daxil edin", validators = [DataRequired()])
    remember_me = BooleanField("Yadda saxla")
    submit = SubmitField("Giris edin")

class RegisterForm(FlaskForm):
    email = EmailField("Emailinizi daxil edin", validators = [DataRequired(),
                                                              custom_blacklist_checker,
                                                              custom_user_checker])
    password = PasswordField("Parolu daxil edin", validators = [DataRequired()])
    confirm_password = PasswordField("Parolu daxil edin", validators = [DataRequired(), 
                                                                        EqualTo("password", "Two passwords are not same")])
    
    name = StringField("Adinizi daxil edin",  validators = [DataRequired(), Length(2,30)])
    surname = StringField('Soyadinizi daxil edin',  validators = [DataRequired(), Length(3,40)])
    submit = SubmitField("Qeydiyyatdan kecin")