import csv
import sys
csv.field_size_limit(sys.maxsize)

def create_word_definition_dict(csv_file):
    word_dict = {}
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            word, _, definition = row
            word_dict[word] = definition
    return word_dict

word_dict = create_word_definition_dict('english-Dictionary.csv')