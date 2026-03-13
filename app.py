# Import
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create app
app = Flask(__name__)
Scss(app)

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

# Database model
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    competed = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.id} - {self.content}"

with app.app_context():
    db.create_all()
    
# Routes to webpages
# Home page
@app.route('/', methods=['POST', 'GET'])
def index():
    # Add a Task
    if request.method == 'POST':
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try: 
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
            
    # Display Tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()    
        return render_template('index.html', tasks=tasks)

# Delete a Task
@app.route('/delete/<int:id>')
def delete(id:int):
    task_to_delete = MyTask.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f"ERROR: {e}")
        return f"ERROR: {e}"

# Update a Task
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id:int):
    task = MyTask.query.get_or_404(id)
    
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    else:
        return render_template('update.html', task=task)

# Runner and Debugger
if __name__ == '__main__':    
    app.run(debug=True)