from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for demonstration
learning_materials = [
    {'id': 1, 'title': 'Introduction to Physics', 'type': 'Book'},
    {'id': 2, 'title': 'Chemistry Basics', 'type': 'Video'}
]

mentors = [
    {'id': 1, 'name': 'John Doe', 'specialization': 'Mathematics'},
    {'id': 2, 'name': 'Jane Smith', 'specialization': 'Science'}
]

students = [
    {'id': 1, 'name': 'Alice', 'grade': '10'},
    {'id': 2, 'name': 'Bob', 'grade': '12'}
]

teachers = [
    {'id': 1, 'name': 'Mr. Brown', 'subject': 'Physics'},
    {'id': 2, 'name': 'Ms. White', 'subject': 'Mathematics'}
]

school_details = {
    'name': 'ABC School',
    'location': 'City X',
    'admission_window': '2024-2025',
    'fees_structure': 'Annual fee: $1000'
}

tuition_centers = [
    {'id': 1, 'name': 'Tuition Center A', 'location': 'City X', 'subject': 'Mathematics', 'teacher': 'Mr. Green'},
    {'id': 2, 'name': 'Tuition Center B', 'location': 'City Y', 'subject': 'Science', 'teacher': 'Ms. Blue'}
]

activity_centers = [
    {'id': 1, 'name': 'Art Studio X', 'location': 'City X'},
    {'id': 2, 'name': 'Music School Y', 'location': 'City Y'}
]

training_centers = [
    {'id': 1, 'name': 'Tech Academy A', 'location': 'City X', 'courses': ['Web Development', 'Data Science']},
    {'id': 2, 'name': 'Career Institute B', 'location': 'City Y', 'courses': ['Business Management', 'Marketing']}
]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learning_materials')
def view_learning_materials():
    return render_template('learning_materials.html', materials=learning_materials)

@app.route('/mentors')
def view_mentors():
    return render_template('mentors.html', mentors=mentors)

@app.route('/students')
def view_students():
    return render_template('students.html', students=students)

@app.route('/teachers')
def view_teachers():
    return render_template('teachers.html', teachers=teachers)

@app.route('/school_details')
def view_school_details():
    return render_template('school_details.html', details=school_details)

@app.route('/tuition_centers')
def view_tuition_centers():
    return render_template('tuition_centers.html', centers=tuition_centers)

@app.route('/activity_centers')
def view_activity_centers():
    return render_template('activity_centers.html', centers=activity_centers)

@app.route('/training_centers')
def view_training_centers():
    return render_template('training_centers.html', centers=training_centers)

if __name__ == '__main__':
    app.run(debug=True)
