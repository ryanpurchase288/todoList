from flask import Flask, render_template, redirect, url_for, request
from application import app, db
from application.models import ToDoList
from application.forms import ToDoForm

@app.route('/')
def index():
    return render_template('index.html', todoList = ToDoList.query.all())

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = ToDoForm()
    if form.validate_on_submit():
        new_task= ToDoList(task = form.task.data, complete=False)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/complete/<idNum>')
def complete(idNum):
    task= ToDoList.query.get(idNum)
    task.complete=True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<idNum>')
def incomplete(idNum):
    task= ToDoList.query.get(idNum)
    task.complete=False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<idNum>', methods=['POST', 'GET'])
def update(idNum):
    form = ToDoForm()
    task = ToDoList.query.get(idNum)
    if form.validate_on_submit():
        task.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = task.task
    return render_template('update.html', title='Update your todo', form=form)


@app.route('/delete/<idNum>')
def delete(idNum):
    task_1= ToDoList.query.get(idNum)
    db.session.delete(task_1)
    db.session.commit()
    return redirect(url_for('index'))
