from flask import Flask, request, render_template
import json
import database

app = Flask(__name__)

PROJECTS = 'projects.json'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def all_projects():
    projects = database.load(PROJECTS)
    return render_template('all_projects.html', projects=projects)


@app.route('/techniques')
def techniques():
    projects = database.load(PROJECTS)
    techniques = database.get_techniques(projects)
    return render_template('techniques.html', techniques=techniques)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/project/<int:id>')
def project(id):
    projects = database.load(PROJECTS)
    project = database.get_project(projects, id)
    return render_template('project.html', project=project)


if __name__ == '__main__':
    app.run(debug=True)
