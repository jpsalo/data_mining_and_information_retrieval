import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

from config import DEBUG_MODE, FIGURE_PATH

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


def process_plot(figure, type, data_set_name, name_suffix):
    if (not DEBUG_MODE):
        name_suffix = '_'.join(name_suffix)
        plt.savefig(FIGURE_PATH + data_set_name + '_' + type + '_' + name_suffix + '.png')


# Mean absolute deviation
def calculate_mean_absolute_deviation(data, attribute, data_set_name, attribute_name):
    print(data_set_name + ':\n' + 'Mean absolute deviation for ' + attribute_name + ' is ' + str(
        pd.Series(data[attribute]).mad()))
