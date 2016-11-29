import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

import json
import csv
import random


from config import DEBUG_MODE, OUTPUT_PATH, FIGURE_PATH

# Suppress SettingWithCopyWarning
# http://stackoverflow.com/a/20627316
pd.options.mode.chained_assignment = None


def calculate_lengths(data, attribute):
    values = data[attribute]
    values_lengths = list(map(lambda x: len(x), values))
    return pd.Series(values_lengths).value_counts().sort_index()


# http://stackoverflow.com/a/14451264
# http://stackoverflow.com/a/16949498
def generate_bins(values):
    bins = np.linspace(values.min(), values.max(), 20)
    return pd.cut(values, bins).value_counts().sort_index()


def get_weekday_frequencies(blogs):
    # http://stackoverflow.com/a/11287278
    return blogs.ix[:, 269:275].sum()


def parse_time(value):
    # http://stackoverflow.com/a/16139085
    value_datetime = datetime.strptime(value, "%m/%d/%Y %H:%M")
    return value_datetime.time()


# Mean absolute deviation
def calculate_mean_absolute_deviation(data, attribute, data_set_name, attribute_name):
    print(data_set_name + ':\n' + 'Mean absolute deviation for ' + attribute_name + ' is ' + str(
        pd.Series(data[attribute]).mad()))


def process_plot(figure, type, data_set_name, name_suffix=None):
    if (not DEBUG_MODE):
        path = FIGURE_PATH + data_set_name + '_' + type
        if name_suffix is not None:
            path = path + '_' + '_'.join(name_suffix)
        plt.savefig(path + '.pdf')


def save_to_json(data, name):
    with open(OUTPUT_PATH + name + '.json', 'w') as outfile:
        # http://stackoverflow.com/a/20776329/7010222
        json.dump(data, outfile, sort_keys=True, indent=2)


def get_sample_transactions(data_path, fraction, tsv=False):

    with open(data_path) as data_file:

        if tsv:
            data_reader = csv.reader(data_file, delimiter='\t')
        else:
            data_reader = csv.reader(data_file)

        rows = sum(1 for row in data_file)
        sample_size = round(rows * fraction)
        skip = sorted(random.sample(range(rows), rows - sample_size))

        data_file.seek(0)
        transactions = []
        for index, row in enumerate(data_reader):
            if index not in skip:
                transaction = []
                for item in row:
                    if item not in transaction:
                        # Only unique values
                        transaction.append(item)
                transactions.append(transaction)

        return transactions
