import json


def all_paths() -> str:
    for path in ['ord_till_sjöss_data.txt', 'sjötermer_data.txt', 'torbjörn_data.txt', 'lär_dig_mer_om_skeppsord_data.txt']:
        yield path


def get_db():
    with open('ord_till_sjöss.json', 'r', encoding='utf8') as f:
        return json.load(f)


def add_to_db(db, data):
    added = 0
    for new_word in data['words']:
        add = True
        for old_word in db['words']:
            if new_word['word'] == old_word['word']:
                add = False
                break
        if add:
            added += 1
            db['words'].append(new_word)
    for new_category in data['categories']:
        add = True
        for old_category in db['categories']:
            if new_category == old_category:
                add = False
                break
        if add:
            db['categories'].append(new_category)
    print('Added %d new words to db' % added)
    return db


def save_db(db):
    with open('ord_till_sjöss.json', 'w') as f:
        f.seek(0)
        f.truncate()
        json.dump(db, f)


def parse_ord_till_sjoss(data):
    d = {'words': [], 'categories': []}
    for line in data:
        if line and len(line) > 1:
            words = line.split()
            word = ''.join(words[:1])
            description = ' '.join(words[1:])
            description = description.lstrip('- ')
            description = description.capitalize()
            category = ''
            d['words'].append({'word': word, 'description': description, 'category': category})
            if category not in d['categories']:
                d['categories'].append(category)
    return d


def parse_sjotermer(data):
    d = {'words': [], 'categories': []}
    for line in data:
        if line and len(line) > 1:
            words = line.split()
            word = ''.join(words[:1]).capitalize().rstrip('.')
            if 'Exempel' in word:
                continue
            description = ' '.join(words[1:])
            description = description.lstrip(' ')
            description = description.capitalize()
            category = ''
            d['words'].append({'word': word, 'description': description, 'category': category})
            if category not in d['categories']:
                d['categories'].append(category)
    return d


if __name__ == '__main__':
    for path in all_paths():
        print('Parsing %s' % path)
        with open(path, 'r', encoding="utf8") as f:
            data = f.read().split('\n')
        if path == 'ord_till_sjöss_data.txt':
            json_data = parse_ord_till_sjoss(data)
        elif path == 'sjötermer_data.txt':
            json_data = parse_sjotermer(data)
        else:
            continue
        db = get_db()
        db = add_to_db(db, json_data)
        print(db)
        # save_db(db)
