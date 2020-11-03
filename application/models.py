from application import db

class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), nullable =False)
    complete = db.Column(db.Integer, nullable=False)

