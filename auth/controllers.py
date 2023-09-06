from flask import Blueprint, render_template, request, flash, \
    redirect, url_for

auth = Blueprint("auth", __name__)

from werkzeug.security import check_password_hash

from flask_login import login_user, login_required, logout_user, current_user

from auth.forms import LoginForm, RegisterForm
from auth.models import User


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if request.method == 'POST':
        if form.validate_on_submit:
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    remember = True if form.remember_me.data else False
                    login_user(user, remember=remember)
                    flash("Login with successfully", "success")
                    return redirect(url_for("auth.profile"))
                
        flash("There are errors", "danger")
        return redirect(url_for("auth.login"))
    
    context = {
        "form": form
    }
    return render_template("login.html", **context)

@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit:
            user = User(
                email = form.email.data,
                password = form.password.data,
                name = form.name.data,
                surname = form.surname.data,
            )
            user.save()

            flash("Register with successfully", "success")
            return redirect(url_for("auth.login"))
        
        flash("There are errors", "danger")
        return redirect(url_for("auth.register"))

    context = {
        "form": form
    }
    return render_template("register-user.html", **context)

@auth.route("/profile", methods=['GET'])
@login_required
def profile():
    user = current_user
    context = {
        "user": user
    }
    return render_template("profile.html", **context)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout with successfully", "success")
    return redirect(url_for("auth.login"))