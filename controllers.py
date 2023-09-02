from flask import render_template, request, flash, redirect, url_for

from app import app
from models import Students
from extensions import db
from forms import RegisterForm

from sqlalchemy import or_


@app.route("/students/")
def students():
    student_count:int = None
    q:str = None
    students = Students.query.all()
    # students = Students.query.order_by(Students.name.asc())
    # students = Students.query.filter_by(status='active')
    if request.args.get("q"):
        # id = request.args.get("q")
        # students = Students.query.filter_by(id=id)
        # students = Students.query.filter(Students.id==id)

        q = request.args.get("q")
        # students = Students.query.filter(Students.name==q)

        q = "%{q}%".format(q=q)
        # students = Students.query.filter(Students.name.like(q)).all()
        # students = Students.query.filter(Students.name.like(q), Students.surname.like(q)).all()  # and yazilisi
        students = Students.query.filter(or_(Students.name.like(q), 
                                             Students.surname.like(q),
                                             Students.bio.like(q),
                                             Students.id > 18)).all()  # or yazilisi

        student_count = len(students)
        q=q[1:len(q)-1]
    return render_template('students.html', students = students, 
                           student_count=student_count, 
                           q=q)


@app.route("/students/<int:id>")
def students_detail(id):
    # student = Students.query.get(id)
    student = db.get_or_404(Students, id)

    # student.view_count += 1
    # db.session.commit()
    return render_template('student_detail.html', student = student)


@app.route("/students/create", methods=["POST", "GET"])
def create_student():
    message:str = None

    if request.method == "POST":
        student = Students(
            name = request.form["name"],
            surname = request.form["surname"],
            gender = request.form["gender"],
            status = request.form["status"],
            bio = request.form["bio"]
        )
        student.save()
        message = "User is created successfully!"
    return render_template('create_student.html', message=message)


@app.route("/students/update/<int:id>", methods=["POST", "GET"])
def update_student(id):
    student = Students.query.filter_by(id=id)
    message:str = None
    if request.method == "POST":

        # new_student = Students(
        #     name = request.form["name"],
        #     surname = request.form["surname"],
        #     gender = request.form["gender"],
        #     status = request.form["status"],
        #     bio = request.form["bio"]
        # )
        # new_student.save()
        # student = new_student

        # student.name = request.form["name"]
        # student.surname = request.form["surname"]
        # student.gender = request.form["gender"]
        # student.status = request.form["status"]
        # student.bio = request.form["bio"]

        # student.data = {
        #     "name": request.form["name"],
        #     "surname": request.form["surname"],
        #     "gender": request.form["gender"],
        #     "status": request.form["status"],
        #     "bio": request.form["bio"],
        # }

        Students.query.filter_by(id=id).update(dict(name = request.form["name"], 
                                                    surname = request.form["surname"], 
                                                    gender = request.form["gender"], 
                                                    status = request.form["status"], 
                                                    bio = request.form["bio"],))

        db.session.commit()

        message = "User is updated successfully!"
        return render_template('update_std.html', student = student[0], message=message)

    return render_template('update_std.html', student = student[0], message=message)


@app.route("/students/delete/<int:id>", methods=["POST", "GET"])
def delete_student(id):
    # # Method 1
    # student = Students.query.get(id)
    # db.session.delete(student)
    # db.session.commit()
    message:str = None

    # Method 2
    if request.method == "POST":
        Students.query.filter_by(id=id).delete()
        db.session.commit()
        message = "User with id {id} is deleted".format(id=id)
    return render_template('delete.html', message = message)
    
@app.route("/register", methods=["POST", "GET"])
def register_student():
    form = RegisterForm()
    if form.validate_on_submit():
        student = Students(
            name = form.name.data,
            surname = form.surname.data,
            email = form.email.data,
            gender = form.gender.data,
            password = form.password.data,
            bio = form.bio.data,
            status = form.status.data,

        )

        flash("User created with successfully!", "success")

        student.save()

        return redirect(url_for("students"))
    return render_template("register.html", form=form)
    