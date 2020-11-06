from flask import Flask, render_template, redirect, url_for, request
from application import app, db
from application.models import ToDoList
from application.forms import ToDoForm, OrderTodo

@app.route('/', methods=['POST', 'GET'])
def index():
    form = OrderTodo()
    totals = {
        "total": ToDoList.query.count(),
        "total_completed": ToDoList.query.filter_by(complete=True).count()
    }
    if form.order_with.data == "new":
        taskList = ToDoList.query.order_by(ToDoList.id.desc()).all()
    elif form.order_with.data == "complete":
        taskList = ToDoList.query.order_by(ToDoList.complete.desc()).all()
    elif form.order_with.data == "incomplete":
        taskList = ToDoList.query.order_by(ToDoList.complete).all()
    else:
        taskList = ToDoList.query.all()

    return render_template('index.html' , taskList=taskList, form=form, totals=totals)

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
