import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from os.path import expanduser

# http://stackoverflow.com/a/4028943
home = expanduser("~")

matplotlib.style.use('ggplot')

DEBUG_MODE = False

BASE_PATH = home + '/Dropbox/koulu/data_mining_and_information_retrieval/'
FIGURE_PATH = BASE_PATH + 'figures/'

posts = pd.read_csv(BASE_PATH + 'HN_posts_year_to_Sep_26_2016.csv')
blogs = pd.read_csv(BASE_PATH + 'BlogFeedback/blogData_train.csv', header=None)

# NOMINAL, ORDINAL

# Frequencies

# TODO: NOMINAL

# HTTP/HTTPS

# ORDINAL


def generate_frequency(values, title, x_label):
    values_df = pd.Series(values).value_counts().sort_index()

    fig = plt.figure()
    plot = values_df.plot.bar(title=title)
    plot.set_xlabel(x_label)
    plot.set_ylabel('Frequency')
    return fig


# QUANTITATIVE


# Distributions
def generate_histogram(data, attribute, title, x_label):
    # Number of comments the posts received
    values = data[attribute]

    fig = plt.figure()
    # http://stackoverflow.com/a/21033789
    plot = values.plot.hist(title=title, bins=20, bottom=0.1, logy=True)
    plot.set_xlabel(x_label)
    plot.set_ylabel('Frequency (log)')
    return fig


# Standard deviation
def generate_standard_deviation(data, attribute, title):
    values = data[attribute]
    means = values.mean()
    errors = values.std()
    fig, ax = plt.subplots()
    pd.Series(means).plot.bar(title=title, yerr=errors, ax=ax, logy=True)
    return fig


# Mean absolute deviation
def calculate_mean_absolute_deviation(data, attribute):
    print(pd.Series(data[attribute]).mad())


# Location
def generate_box_plot(data, attribute, x_label, hide_fliers=False):
    values_df = pd.DataFrame(data[attribute])
    title = 'Quartiles (without outliers)' if hide_fliers else 'Quartiles'

    fig = plt.figure()

    plot = values_df.boxplot(return_type='axes', showfliers=not hide_fliers)
    plot.set_yscale('log')
    plt.xticks([1], [x_label])

    plot.set_title(title)
    plot.set_ylabel('log')
    return fig


def calculate_lengths(data, attribute):
    values = data[attribute]
    values_lengths = list(map(lambda x: len(x), values))
    return values_lengths


def process_plot(figure, type, name_suffix):
    if (not DEBUG_MODE):
        plt.savefig(FIGURE_PATH + type + '_' + name_suffix + '.png')


# Lengths of the blog post titles
posts_title_lengths = calculate_lengths(posts, 'title')

frequency_figure = generate_frequency(posts_title_lengths, 'Lengths of the titles', 'Length (characters)')
process_plot(frequency_figure, 'frequency', 'title_lengths')
#
histogram_figure = generate_histogram(posts, 'num_comments', 'Number of comments the posts received', 'Comments')
process_plot(histogram_figure, 'histogram', 'comments')

calculate_mean_absolute_deviation(posts, 'num_comments')

standard_deviation_figure = generate_standard_deviation(posts, 'num_comments',
                                                        'Standard deviation of the number of comments')
process_plot(standard_deviation_figure, 'standard_deviation', 'comments')

box_plot_figure = generate_box_plot(posts, 'num_points', 'Comments')
process_plot(box_plot_figure, 'box_plot', 'comments')

box_plot_without_outliers_figure = generate_box_plot(posts, 'num_points', 'Comments',  True)
process_plot(box_plot_without_outliers_figure, 'box_plot', 'comments_without_outliers')

# For presentation and debug
# http://stackoverflow.com/a/25163682
plt.show()
