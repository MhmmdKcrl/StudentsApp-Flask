from flask_admin.contrib.sqla import ModelView

from extensions import admin, db

from auth.models import User, Role
from student.models import Students
from blog.models import Blog

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Students, db.session))
admin.add_view(ModelView(Blog, db.session))
