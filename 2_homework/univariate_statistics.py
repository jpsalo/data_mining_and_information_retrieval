import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from os.path import expanduser

# http://stackoverflow.com/a/4028943
home = expanduser("~")

matplotlib.style.use('ggplot')

BASE_PATH = home + '/Dropbox/koulu/data_mining_and_information_retrieval/'
FIGURE_PATH = BASE_PATH + 'figures/'

posts = pd.read_csv(BASE_PATH + 'HN_posts_year_to_Sep_26_2016.csv')

# NOMINAL, ORDINAL

# Frequencies

# TODO: NOMINAL

# HTTP/HTTPS

# ORDINAL


def generate_frequency(values, title, x_label, name_suffix):
    values_df = pd.Series(values).value_counts().sort_index()

    plt.figure(1)
    plot = values_df.plot.bar(title=title)
    plot.set_xlabel(x_label)
    plot.set_ylabel('Frequency')
    plt.savefig(FIGURE_PATH + 'frequency_' + name_suffix + '.png')

# QUANTITATIVE


# Distributions
def generate_histogram(data, attribute, title, x_label, name_suffix):
    # Number of comments the posts received
    values = data[attribute]

    plt.figure(2)
    # http://stackoverflow.com/a/21033789
    plot = values.plot.hist(title=title, bins=20, bottom=0.1, logy=True)
    plot.set_xlabel(x_label)
    plot.set_ylabel('Frequency (log)')
    plt.savefig(FIGURE_PATH + 'histogram_' + name_suffix + '.png')


# Standard deviation
def generate_standard_deviation(data, attribute, title, name_suffix):
    values = data[attribute]
    means = values.mean()
    errors = values.std()
    fig, ax = plt.subplots()
    pd.Series(means).plot.bar(title=title, yerr=errors, ax=ax, logy=True)
    plt.savefig(FIGURE_PATH + 'standard_deviation_' + name_suffix + '.png')


# Mean absolute deviation
def calculate_mean_absolute_deviation(data, attribute):
    print(pd.Series(data[attribute]).mad())


# Location
def generate_box_plot(data, attribute, x_label, name_suffix, hide_fliers=False):
    values_df = pd.DataFrame(data[attribute])
    title = 'Quartiles (without outliers)' if hide_fliers else 'Quartiles'

    plot = values_df.plot.box(title=title, showfliers=not hide_fliers, logy=True)
    plt.xticks([1], [x_label])
    plot.set_ylabel('log')
    plt.savefig(FIGURE_PATH + 'box_plot_' + name_suffix + '.png')


def calculate_lengths(data, attribute):
    values = data[attribute]
    values_lengths = list(map(lambda x: len(x), values))
    return values_lengths


# Lengths of the blog post titles
posts_title_lengths = calculate_lengths(posts, 'title')

generate_frequency(posts_title_lengths, 'Lengths of the titles', 'Length (characters)', 'title_lengths')
generate_histogram(posts, 'num_comments', 'Number of comments the posts received', 'Comments', 'comments')
calculate_mean_absolute_deviation(posts, 'num_comments')
generate_standard_deviation(posts, 'num_comments', 'Standard deviation of the number of comments', 'comments')
generate_box_plot(posts, 'num_points', 'Comments', 'comments')
generate_box_plot(posts, 'num_points', 'Comments', 'comments_without_outliers',  True)

# For presentation and debug
# http://stackoverflow.com/a/25163682
# plt.show()
