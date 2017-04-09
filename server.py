from flask import Flask, request, render_template
import json
import database

app = Flask(__name__)

DATABASE = 'projects.json'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/projects')
def all_projects():
    projects = database.load(DATABASE)
    return render_template('all_projects.html', projects=projects)


@app.route('/techniques')
def techniques():
    projects = database.load(DATABASE)
    techniques = database.get_techniques(projects)
    return render_template('techniques.html', techniques=techniques)


@app.route('/project/<int:id>')
def project(id):
    projects = database.load(DATABASE)
    project = database.get_project(projects, id)
    return render_template('project.html', project=project)

@app.route('/addproject', methods=['POST'])
def add_project():
    project = request.form['project']
    db = database.load(DATABASE)

if __name__ == '__main__':
    app.run(debug=True)
