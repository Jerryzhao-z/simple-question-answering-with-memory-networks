import json
import os.path as path

# Get project settings
settings_f_name = path.join(path.dirname(path.realpath(__file__)), '..', 'SETTINGS.json')


def clean_words(words):
    for w in words:
        w = w.strip('".\'?)(:,!\\[]=/')
        if w.endswith('\'s'):
            w = w[:len(w)-2]
        yield w


with open(settings_f_name) as settings_f:
    settings = json.load(settings_f)
    datasets = ['train', 'test', 'validate']
    words = set()
    for ds in datasets:
        with open(settings['train']) as in_f:
            for line in in_f:
                words.update(clean_words(line.split('\t')[3].strip().lower().split(' ')))

    words.remove('')

    vocabulary = list(words)
    vocabulary.sort()
    with open(settings['vocabulary'], mode='w') as out_f:
        for v in vocabulary:
            print(v, file=out_f)
