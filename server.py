from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/techniques')
def techniques():
    return render_template('techniques.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
