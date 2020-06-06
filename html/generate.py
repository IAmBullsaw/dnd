
import json
from pathlib import Path

if __name__ == '__main__':
    db = None
    data_folder = Path('../data/')

    with open(data_folder / 'data.json', 'r', encoding='utf8') as f:
        db = json.load(f)

    beginning = """<!DOCTYPE html>
<html>
  <head>
    <title>Sjötermer</title>
    <meta charset="UTF-8">
  </head>
  <body>
  """
    end = """</body>
</html>
"""
    with open('index.html', 'w', encoding='utf8') as f:
        f.write(beginning)
        for category in sorted(db['categories']):
            f.write('<div class="category">')
            f.write('<h1 class="header">{}</h1>'.format(category.capitalize()))
            f.write('<ul>')
            for word in sorted(db['words'], key=lambda w: w['word']):
                if category == word['category']:
                    line = '<li><h2 class="word">{}</h2> <span class="description">{}</span></li>'.format(word['word'], word['description'])
                    f.write(line)
            f.write('</ul>')
        f.write(end)
