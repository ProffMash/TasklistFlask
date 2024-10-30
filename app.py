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
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
    },
    {
        'id': 3,
        'title': 'Learn Flask',
        'description': 'Need to find a good Flask tutorial on the web',
    }
]

#routes
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
     if request.method == 'POST':
        new_id=len(tasks)+1
        title = request.form['title']
        description = request.form['description']
        tasks.append({'id': new_id, 'title': title, 'description': description, 'done': False})
        return redirect(url_for('index'))
    
@app.route('/delete/<int:id>')
def delete(id):
    global tasks
    tasks = [task for task in tasks if task['id'] !=id]
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=["GET","POST"])
def edit(id):
    task = next((task for task in tasks if task['id'] == id), None)
    print(task)
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)
        
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)