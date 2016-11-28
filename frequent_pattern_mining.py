import csv
import apyori

import utilities


def apriori(data_path, name):
    with open(data_path) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter='\t')
        results = list(apyori.apriori(tsvreader))
        utilities.save_to_json(results, name)
