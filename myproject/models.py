from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Task(db.Model):
    __tablename__ = "task"
    task_id = db.Column(db.Integer, primary_key=True)
    issued_by = db.Column(db.String(64))
    issued_to = db.Column(db.String(64))
    issued_time = db.Column(db.String(64))
    due_time = db.Column(db.String(64))
    completed = db.Column(db.Integer())

    def __init__(self, issued_by, issued_to, issued_time, due_time, completed):
        self.issued_by = issued_by
        self.issued_to = issued_to
        self.issued_time = issued_time
        self.due_time = due_time
        self.completed = completed