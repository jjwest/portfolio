import json

def load(filename='data.json'):
    try:
        with open(filename) as db:
            json_data = json.load(db)
            json_data.sort(key=lambda r: r['project_no'])
            return json_data
    except:
        return None


def get_project_count(db):
    return len(db)


def get_project(db, id):
    for project in db:
        if project['project_no'] == id:
            return project
    return None


def get_techniques(db):
    techniques_used = []
    for project in db:
        for technique in project['techniques_used']:
            if technique.upper() not in techniques_used:
                techniques_used.append(technique.upper())
                techniques_used.sort()
    return techniques_used
