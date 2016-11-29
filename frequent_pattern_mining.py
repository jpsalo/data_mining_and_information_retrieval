import json

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import apyori as apriori
from fp_growth import find_frequent_itemsets

import utilities


def frequent_itemsets_apriori(data_path, name, fraction, minimum_support):
    data_sample = utilities.get_sample_transactions(data_path, fraction, True)
    results = list(apriori.apriori(data_sample, min_support=minimum_support))

    # http://stackoverflow.com/a/38515465/7010222
    output = []
    for RelationRecord in results:
        o = StringIO()
        apriori.dump_as_json(RelationRecord, o)
        output.append(json.loads(o.getvalue()))

    utilities.save_to_json(output, name + '_apriori_' + str(minimum_support))


def frequent_itemsets_fp_growth(data_path, name, fraction, minimum_support_frequency):
    transactions_sample = utilities.get_sample_transactions(data_path, fraction)

    result = []
    number_of_transactions = len(transactions_sample)
    minimum_support = number_of_transactions * minimum_support_frequency

    for itemset, support in find_frequent_itemsets(transactions_sample, minimum_support, True):
        support_frequency = support / number_of_transactions
        result.append((itemset, support_frequency))

    result = sorted(result, key=lambda i: i[0])

    output = []
    for itemset, support_frequency in result:
        output.append({
            "itemset": itemset,
            "support": support_frequency
            })

    utilities.save_to_json(output,  name + '_fp_growth_' + str(minimum_support_frequency))
