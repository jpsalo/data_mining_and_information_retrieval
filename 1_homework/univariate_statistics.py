import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

posts = pd.read_csv('~/Dropbox/koulu/data_mining_and_information_retrieval/HN_posts_year_to_Sep_26_2016.csv')
posts_sample = posts.sample(n=100)

# NOMINAL, ORDINAL

# Frequencies

# TODO: NOMINAL

# HTTP/HTTPS

# ORDINAL


def generate_frequency(values, title, x_label):
    values_df = pd.Series(values).value_counts().sort_index()

    plt.figure(1)
    plot = values_df.plot.bar(title=title)
    plot.set_xlabel(x_label)
    plot.set_ylabel('Frequency')

# QUANTITATIVE


# Distributions
def generate_histogram(data, attribute, title, x_label):
    # Number of comments the posts received
    values = data[attribute]

    plt.figure(2)
    plot = values.plot.hist(title=title, bins=20)
    plot.set_xlabel(x_label)
    plot.set_ylabel('Frequency')


# Standard deviation
def generate_standard_deviation(data, attribute):
    values = data[attribute]
    means = values.mean()
    errors = values.std()
    plt.figure(3)
    fig, ax = plt.subplots()
    pd.Series(means).plot.bar(yerr=errors, ax=ax)


# Mean absolute deviation
def calculate_mean_absolute_deviation(data, attribute):
    values = pd.Series(data[attribute]).mad()


# Location
def generate_box_plot(data, attribute):
    values_df = pd.DataFrame(data[attribute])

    plt.figure(4)
    values_df.plot.box(showfliers=False)
    plt.figure(5)
    values_df.plot.box()


def calculate_lengths(data, attribute):
    values = data[attribute]
    values_lengths = list(map(lambda x: len(x), values))
    return values_lengths


# Lengths of the blog post titles
posts_title_lengths = calculate_lengths(posts, 'title')

generate_frequency(posts_title_lengths, 'Lengths of the titles', 'Length (characters)')
generate_histogram(posts, 'num_comments', 'Number of comments the posts received', 'Comments')
generate_standard_deviation(posts, 'num_comments')
calculate_mean_absolute_deviation(posts, 'num_comments')
generate_box_plot(posts, 'num_points')

# http://stackoverflow.com/a/25163682
plt.show()
