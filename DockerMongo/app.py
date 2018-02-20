import os
import flask
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

# http://127.0.0.1:5000

app = Flask(__name__)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb # gets database

db.tododb.delete_many({})

@app.route('/')
def todo():
    return render_template('todo.html') # updates displayed items
    # todo.html has two blank text boxes and a submit button
    # entering text in the left box and hitting submit will
    # display it below in large bold while data entered in
    # right box displays it below in smaller unbolded letters
    # left box contents are displayed before right box contents

@app.route('/display', methods=['POST'])
def display():
    _items = db.tododb.find() # finds specified data base collection?
    items = [item for item in _items] 	
    # contents of text box are kept track of in items (saved)
    # and then displayed below

    return render_template('times.html',items=items) # updates displayed items
    # todo.html has two blank text boxes and a submit button
    # entering text in the left box and hitting submit will
    # display it below in large bold while data entered in
    # right box displays it below in smaller unbolded letters
    # left box contents are displayed before right box contents

@app.route('/new', methods=['POST'])
def new():
    item_doc = {
        'name': request.form['name'],
		'description': request.form['description']
    }
    db.tododb.insert_one(item_doc) # inserts both items from text boxes into db
    return redirect(url_for('todo')) # calls todo method again

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
