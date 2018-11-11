import csv
from FuzzyApp.models import Word
def load_word(file_path):
    "this loads drugs from pipe delimited file with headers"
    reader = csv.DictReader(open(file_path))
    for row in reader:
        drug = Word(word=row['word'], frequency=row['freq'])
        drug.save()