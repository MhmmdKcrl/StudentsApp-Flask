from extensions import db

from sqlalchemy.orm import backref

from student.models import Students

class Blog(db.Model):
    __tablename__ = "blog"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    text = db.Column(db.Text, nullable=False, default = "some text")

    students_id = db.Column(db.Integer, db.ForeignKey(Students.id))
    students = db.relationship(Students, backref =backref("students", uselist=True))


    def __repr__(self):
        return self.title
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    