import apyori

import utilities


def apriori(data, name):
    head = [next(data) for x in range(2)]

    results = list(apyori.apriori(head))
    utilities.save_to_json(results, name)
