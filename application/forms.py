from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired, ValidationError
from application.models import ToDoList

class ToDoCheck:
    def __init__(self,message):
        self.message = message

    def __call__(self, form, field):
        all_todos = ToDoList.query.all()
        for todo in all_todos:
            if todo.task == field.data:
                raise ValidationError(self.message)

class ToDoForm(FlaskForm):
    task = StringField('Task', validators = [DataRequired()
        ,ToDoCheck(message='You have repeated a to do')
        ])
    submit =SubmitField('Submit')
   

