from extensions import db
from datetime import datetime
from sqlalchemy.orm import backref

class Students(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.Text, nullable=True)
    password = db.Column(db.Text, nullable=True)
    surname = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    status = db.Column(db.String(8), nullable=True)
    image = db.Column(db.Text, nullable=True, default="some image path")
    bio = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable = True, default = datetime.utcnow)

    def __repr__(self):
        return self.name
    
    # def __str__(self):
    #     return self.name
    
    # def __init__(self, name, surname, gender, status, image, bio):
    #     self.name = name
    #     self.surname = surname
    #     self.gender = gender
    #     self.status = status
    #     self.image = image
    #     self.bio = bio
                
    
    def save(self):
        db.session.add(self)
        db.session.commit()


# student = Students("Orxan","Aliyev","male","active","images/image2", "Orxans bio")

# query.all()  # list verir
# query.get(2)
# query.filter_by(name='Ali')  # list verir

class Blog(db.Model):
    __tablename__ = "blog"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    text = db.Column(db.Text, nullable=False, default = "some text")

    students_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    students = db.relationship("Students", backref =backref("students", uselist=False))


    def __repr__(self):
        return self.title
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    