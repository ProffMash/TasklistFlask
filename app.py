#decorator app.route(), used for url mapping
from flask import Flask, render_template, request, redirect, url_for

#initialize the app
app = Flask(__name__)

#list of dictionaries to represent records
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    },
    {
        'id': 3,
        'title': 'Learn Flask',
        'description': 'Need to find a good Flask tutorial on the web',
        'done': False
    }
]

#routes
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)