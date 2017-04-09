import json

def load(filename='data.json'):
    try:
        with open(filename) as db:
            data = json.load(db)
            return data
    except:
        return None

def add_project(db, project, filename):
    db.append(project)
    with open(filename, 'w') as f:
        f.write(db)

def get_project_count(db):
    return len(db)


def get_project(db, id):
    for project in db:
        if project['id'] == id:
            return project
    return None


def get_techniques(db):
    techniques_used = []
    for project in db:
        for technique in project['techniques']:
            if technique not in techniques_used:
                techniques_used.append(technique)
                techniques_used.sort()
    return techniques_used
