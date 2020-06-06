import json
import os

def all_files() -> str:
    for path in ['ord_till_sjöss_data.txt']:
        yield path

def get_db():
    return json.load('ord_till_sjöss.json')

def add_to_db(db, data):
    pass

def save_db(db):
    with open('ord_till_sjöss.json','w') as f:
        f.seek(0)
        f.truncate()
        f.write(json.dump(db))

if __name__ == '__main__':
    for path in all_files():
        with open(path,'r') as f:
            data = f.read()
        if path == 'ord_till_sjöss_data.txt':
            json_data = parse_ordTillSjoss(data)
        db = get_db()
        add_to_db(db, json_data)
        save_db(db)
