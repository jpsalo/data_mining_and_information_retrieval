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

def generate_frequency():
    # Lengths of the blog post titles
    titles = posts['title']

    title_lengths = list(map(lambda x: len(x), titles))

    title_lengths_df = pd.Series(title_lengths).value_counts().sort_index()

    plt.figure(1)
    plot = title_lengths_df.plot.bar(title='Lengths of the titles')
    plot.set_xlabel('Length (characters)')
    plot.set_ylabel('Frequency')

generate_frequency()

# QUANTITATIVE

# Distributions
def generate_histogram():
    # Number of comments the posts received
    comments = posts['num_comments']

    plt.figure(2)
    plot = comments.plot.hist(title='Number of comments the posts received', bins=20)
    plot.set_xlabel('Comments')
    plot.set_ylabel('Frequency')

generate_histogram()


# Standard deviation
def generate_standard_deviation():
    comments = posts['num_comments']
    means = comments.mean()
    errors = comments.std()
    plt.figure(3)
    fig, ax = plt.subplots()
    pd.Series(means).plot.bar(yerr=errors, ax=ax)

generate_standard_deviation()


# Mean absolute deviation
def calculate_mean_absolute_deviation():
    comments = posts['num_comments']
    pd.Series(comments).mad()

calculate_mean_absolute_deviation()


# Location
def generate_box_plot(data, attribute):
    values_df = pd.DataFrame(data[attribute])

    plt.figure(4)
    values_df.plot.box(showfliers=False)
    plt.figure(5)
    values_df.plot.box()

generate_box_plot(posts, 'num_points')

# http://stackoverflow.com/a/25163682
plt.show()
