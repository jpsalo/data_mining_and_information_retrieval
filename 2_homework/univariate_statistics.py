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


def get_data_set_name(data_set):
    name = ''
    if data_set == 'posts':
        name = 'hacker_news_posts'
    elif data_set == 'blogs':
        name = 'blog_posts'
    return name

# NOMINAL, ORDINAL

# Frequencies

# TODO: NOMINAL

# HTTP/HTTPS

# ORDINAL


def generate_frequency(values, data_set_name, title, x_label):
    title = title + '\n' + data_set_name
    values_df = values.value_counts().sort_index()

    fig = plt.figure()
    plot = values_df.plot.bar(title=title)
    plot.set_xlabel(x_label)
    plot.set_ylabel('Frequency')
    return fig

# QUANTITATIVE


# Distributions
def generate_histogram(data, attribute, data_set_name, title, x_label, log_scale=False):
    title = title + '\n' + data_set_name
    values = data[attribute]

    fig = plt.figure()
    # http://stackoverflow.com/a/21033789
    plot = values.plot.hist(title=title, bins=20, bottom=0.1, logy=log_scale)
    plot.set_xlabel(x_label)
    y_label = 'Frequency (log)' if log_scale else 'Frequency'
    plot.set_ylabel(y_label)
    return fig


# Standard deviation
def generate_standard_deviation(data, attribute, data_set_name, title, log_scale=False):
    title = title + '\n' + data_set_name
    values = data[attribute]
    means = values.mean()
    errors = values.std()
    fig, ax = plt.subplots()
    plot = pd.Series(means).plot.bar(title=title, yerr=errors, ax=ax, logy=log_scale)
    if log_scale:
        plot.set_ylabel('log')
    return fig


# Mean absolute deviation
def calculate_mean_absolute_deviation(data, attribute, data_set_name, attribute_name):
    print(data_set_name + ':\n' + 'Mean absolute deviation for ' + attribute_name + ' is ' + str(
        pd.Series(data[attribute]).mad()))


# Location
def generate_box_plot(data, attribute, data_set_name, x_label, hide_fliers=False, log_scale=False):
    values_df = pd.DataFrame(data[attribute])
    title = ('Quartiles (without outliers)' if hide_fliers else 'Quartiles') + '\n' + data_set_name

    fig = plt.figure()

    plot = values_df.boxplot(return_type='axes', showfliers=not hide_fliers)
    if log_scale:
        plot.set_yscale('log')
        plot.set_ylabel('log')
    plt.xticks([1], [x_label])

    plot.set_title(title)
    return fig


def calculate_lengths(data, attribute):
    values = data[attribute]
    values_lengths = list(map(lambda x: len(x), values))
    return pd.Series(values_lengths)


# http://stackoverflow.com/a/14451264
# http://stackoverflow.com/a/16949498
def generate_bins(values):
    bins = np.linspace(values.min(), values.max(), 20)
    return pd.cut(values, bins)


def process_plot(figure, type, data_set_name, name_suffix):
    if (not DEBUG_MODE):
        plt.savefig(FIGURE_PATH + data_set_name + '_' + type + '_' + name_suffix + '.png')


# Lengths of the blog post titles
posts_title_lengths = calculate_lengths(posts, 'title')
frequency_figure = generate_frequency(posts_title_lengths, get_data_set_name('posts'), 'Lengths of the titles',
                                      'Length (characters)')
process_plot(frequency_figure, 'frequency', get_data_set_name('posts'), 'title_lengths')

# Lengths of the blog posts
blog_text_lengths = generate_bins(blogs[61])
frequency_figure = generate_frequency(blog_text_lengths, get_data_set_name('blogs'), 'Lengths of the blog posts',
                                      'Length (characters)')
process_plot(frequency_figure, 'frequency', get_data_set_name('blogs'), 'post_lengths')

histogram_figure = generate_histogram(posts, 'num_comments', get_data_set_name('posts'),
                                      'Number of comments the posts received', 'Comments', True)
process_plot(histogram_figure, 'histogram', get_data_set_name('posts'), 'comments')

histogram_figure = generate_histogram(blogs, 50, get_data_set_name('blogs'), 'Total number of comments before basetime',
                                      'Comments', True)
process_plot(histogram_figure, 'frequency', get_data_set_name('blogs'), 'comments')

calculate_mean_absolute_deviation(posts, 'num_comments', get_data_set_name('posts'), 'comments')
calculate_mean_absolute_deviation(blogs, 50, get_data_set_name('blogs'), 'comments')

standard_deviation_figure = generate_standard_deviation(posts, 'num_comments', get_data_set_name('posts'),
                                                        'Standard deviation of the number of comments', True)
process_plot(standard_deviation_figure, 'standard_deviation', get_data_set_name('posts'), 'comments')

standard_deviation_figure = generate_standard_deviation(blogs, 50, get_data_set_name('blogs'),
                                                        'Standard deviation of the number of comments', True)
process_plot(standard_deviation_figure, 'standard_deviation', get_data_set_name('blogs'), 'comments')

box_plot_figure = generate_box_plot(posts, 'num_points', get_data_set_name('posts'), 'Comments', log_scale=True)
process_plot(box_plot_figure, 'box_plot', get_data_set_name('posts'), 'comments')

box_plot_without_outliers_figure = generate_box_plot(posts, 'num_points', get_data_set_name('posts'), 'Comments', True)
process_plot(box_plot_without_outliers_figure, 'box_plot', get_data_set_name('posts'), 'comments_without_outliers')

box_plot_figure = generate_box_plot(blogs, 50, get_data_set_name('blogs'), 'Comments', log_scale=True)
process_plot(box_plot_figure, 'box_plot', get_data_set_name('blogs'), 'comments')

box_plot_without_outliers_figure = generate_box_plot(blogs, 50, get_data_set_name('blogs'), 'Comments', True)
process_plot(box_plot_without_outliers_figure, 'box_plot', get_data_set_name('blogs'), 'comments_without_outliers')

# For presentation and debug
# http://stackoverflow.com/a/25163682
plt.show()
