from collections import defaultdict
import csv
import json

# assert that id_ and url are both keys, and english texts are unique w.r.t. the keys

d = defaultdict(list)

with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"', lineterminator='\n', strict=True)
    next(reader)  # skip header
    for id_, text, english_text, url in reader:
        existing_dict = d[url]
        for id_2, text_2, english_text_2 in existing_dict:
            assert id_ == id_2
            assert english_text == english_text_2
        existing_dict.append((id_, text, english_text))

# process texts

d = defaultdict(dict)  # dict preserves insertion order

with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"', lineterminator='\n', strict=True)
    next(reader)  # skip header
    for id_, text, english_text, url in reader:
        d[id_, english_text, url][text] = None

for x in d.values():
    if len(x) == 3:  # Arabic; Arabic+Vowel; Latin
        print(list(x))
    elif len(x) == 2:  # Arabic; Latin
        pass
    elif len(x) == 1:  # Arabic
        pass
    else:
        raise ValueError

with open('data-postprocessed.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', lineterminator='\n', strict=True)
    writer.writerow(('id', 'url', 'english_text', 'texts'))
    for (id_, english_text, url), texts in d.items():
        writer.writerow((id_, url, english_text, json.dumps(tuple(texts), ensure_ascii=False)))
