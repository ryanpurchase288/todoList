from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired, ValidationError
from application.models import ToDoList


class ToDoForm(FlaskForm):
    task = StringField('Task', validators = [DataRequired()])
    submit =SubmitField('Submit')
   

